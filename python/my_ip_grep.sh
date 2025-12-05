#!/bin/bash

# API endpoint
url="https://api.myip.com/"

# Fetch raw JSON
response=$(curl -s "$url")

# Extract values with grep + cut
ip=$(echo "$response" | grep -o '"ip":"[^"]*"' | cut -d'"' -f4)
country=$(echo "$response" | grep -o '"country":"[^"]*"' | cut -d'"' -f4)
country_code=$(echo "$response" | grep -o '"cc":"[^"]*"' | cut -d'"' -f4)

# Output
echo "Public IP Address: $ip"
echo "Country: $country"
echo "Country Code: $country_code"
