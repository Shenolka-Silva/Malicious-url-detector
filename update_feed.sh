#!/bin/bash
cd ~/url-detector
curl -sL -A "Mozilla/5.0" https://openphish.com/feed.txt -o data/openphish.tmp
if head -n 1 data/openphish.tmp | grep -q '^http'; then
    mv data/openphish.tmp data/openphish.txt
    echo "Feed updated: $(wc -l < data/openphish.txt) URLs"
else
    rm -f data/openphish.tmp
    echo "Update failed, kept the old feed"
fi
