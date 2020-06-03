#!/bin/bash

read -p "Jak długiego zlepku spółgłosek szukasz? " length

filepath='slowa.txt'
consonants='[bcćdfghjklłmnńprstwxzźż]{'$length',}'
doubles='rz|cz|sz|dz|dź|dż|ch'

result=()

while IFS= read -r word; do
  if [[ $word =~ $consonants ]]; then
    frag=$BASH_REMATCH

    doubles_count=$(echo "$frag" | grep -Eo ${doubles} | wc -l)

    if (( ${#frag} - $doubles_count - $length >= 0 )); then
      result+=("$word")
    fi
  fi
done <"$filepath"

echo ${#result[@]}

printf "%s\n" "${result[@]}" > "bash_${length}_consonants.txt"
