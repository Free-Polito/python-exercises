#!/bin/bash

for FILE in *.py;
do
  tail -n +11 "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"
done
