#!/usr/bin/env bash
# Extract http(s) URLs from each skill's SKILL.md and verify they respond.
# Templated URLs (containing { } or ${...}) are skipped: they need real
# parameters such as an API key and cannot be checked anonymously.
#
# Open-API gateway hosts answer 400/401/403 when a URL is called without a
# serviceKey or required query parameters. That still proves the endpoint
# exists - and matches this repo's own verification standard in
# CONTRIBUTING.md ("call without a key and confirm an auth error comes
# back"). For those hosts only 404 (unknown path) or a connection failure
# counts as dead. All other hosts must answer 2xx/3xx.
set -u
fail=0

is_openapi_host() {
  case "$1" in
    *apis.data.go.kr*|*openapi.tago.go.kr*|*odp.airport.kr*|\
*swopenapi.seoul.go.kr*|*openapi.seoul.go.kr*|*ecos.bok.or.kr*|*koreaexim.go.kr*)
      return 0 ;;
    *) return 1 ;;
  esac
}

# Korean public sites known to geo-block or throttle overseas traffic
# (observed from GitHub Actions runners). A persistent connection failure
# to one of these is a WARN, not a dead URL.
is_geo_restricted_host() {
  case "$1" in
    *www.arex.or.kr*|*www.koreaexim.go.kr*|*data.go.kr*|*ecos.bok.or.kr*) return 0 ;;
    *) return 1 ;;
  esac
}

# curl with up to 3 attempts; prints the last HTTP code (000 = no response).
fetch_code() {
  local url="$1" code=000 attempt
  for attempt in 1 2 3; do
    code=$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 30 \
      -A 'tabi-skill-url-check' "$url")
    [ "$code" != "000" ] && break
  done
  printf '%s' "$code"
}

mapfile -t urls < <(grep -hoE 'https?://[^ )"`<]+' -- */SKILL.md \
  | sed 's/[.,;]*$//' | sort -u)
for url in "${urls[@]}"; do
  case "$url" in
    *'{'*|*'}'*) echo "SKIP  $url (templated)"; continue ;;
  esac
  code=$(fetch_code "$url")
  case "$code" in
    2*|3*)
      echo "OK    $code $url" ;;
    000)
      if is_geo_restricted_host "$url"; then
        echo "WARN  $code $url (unreachable from this network; known geo-restricted host)"
      else
        echo "FAIL  $code $url"; fail=1
      fi ;;
    400|401|403)
      if is_openapi_host "$url"; then
        echo "OK    $code $url (endpoint exists; key/params required)"
      else
        echo "FAIL  $code $url"; fail=1
      fi ;;
    *)
      echo "FAIL  $code $url"; fail=1 ;;
  esac
done
exit "$fail"
