#!/bin/bash

# API endpoint
url="https://api.myip.com/"

# Fetch JSON
response=$(curl -s "$url")

# Extract using jq
ip=$(echo "$response" | jq -r '.ip')
country=$(echo "$response" | jq -r '.country')
country_code=$(echo "$response" | jq -r '.cc')

# Output
echo "Public IP Address: $ip"
echo "Country: $country"
echo "Country Code: $country_code"
