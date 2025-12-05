#Python script - system information
#os, cpu, memory, storage, processes

#import platform
#import psutil

#def get_os_info():
    #print("Operating System:")
    #print(platform.system(), platform.release())
    #print()

#!/bin/bash

echo "Operating System:"

# Get OS name
os_name=$(uname -s)

# Get OS release/version
os_version=$(uname -r)

echo "$os_name $os_version"


echo "CPU Information:"

# Processor name
processor=$(uname -p)
# Fallback if uname -p returns "unknown"
if [ "$processor" = "unknown" ]; then
    processor=$(grep -m1 'model name' /proc/cpuinfo | cut -d':' -f2 | xargs)
fi

# Architecture
architecture=$(uname -m)

echo "Processor: $processor"
echo "Architecture: $architecture"

#ps -eo pid,user,comm --no-headers | while read pid user comm; do
#   echo "{'pid': $pid, 'name': '$comm', 'username': '$user'}"
#done


#!/bin/bash

format_size() {
    local size=$1
    local units=("B" "KB" "MB" "GB" "TB")
    local i=0

    # Gebruik bc voor decimale berekening
    while [ "$(echo "$size >= 1024" | bc)" -eq 1 ] && [ $i -lt $((${#units[@]}-1)) ]; do
        size=$(echo "scale=1; $size/1024" | bc)
        ((i++))
    done

    echo "$size ${units[$i]}"
}

# Voorbeeldgebruik
echo "1024 bytes = $(format_size 1024)"
echo "1048576 bytes = $(format_size 1048576)"
