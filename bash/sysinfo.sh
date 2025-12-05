#!/bin/bash

# --- Functies ---
get_os_info() {
    echo "Operating System:"
    echo "$(uname -s) $(uname -r)"
    echo
}

get_cpu_info() {
    echo "CPU Information:"
    processor=$(uname -p)
    if [ "$processor" = "unknown" ]; then
        processor=$(grep -m1 'model name' /proc/cpuinfo | cut -d':' -f2 | xargs)
    fi
    architecture=$(uname -m)
    echo "Processor: $processor"
    echo "Architecture: $architecture"
    echo
}

format_size() {
    local size=$1
    local units=("B" "KB" "MB" "GB" "TB")
    local i=0
    while [ "$(echo "$size >= 1024" | bc)" -eq 1 ] && [ $i -lt $((${#units[@]}-1)) ]; do
        size=$(echo "scale=1; $size/1024" | bc)
        ((i++))
    done
    echo "$size ${units[$i]}"
}

get_memory_info() {
    echo "Memory Information:"
    total=$(grep MemTotal /proc/meminfo | awk '{print $2*1024}')
    available=$(grep MemAvailable /proc/meminfo | awk '{print $2*1024}')
    echo "Total: $(format_size $total)"
    echo "Available: $(format_size $available)"
    echo
}

get_storage_info() {
    echo "Storage Information:"
    df -h --total | grep "total" | awk '{print "Total: "$2", Used: "$3", Available: "$4}'
    echo
}

get_process_info() {
    echo "Process Information:"
    ps -eo pid,user,comm --no-headers | while read pid user comm; do
        echo "{'pid': $pid, 'name': '$comm', 'username': '$user'}"
    done
    echo
}

# --- Main ---
main() {
    get_os_info
    get_cpu_info
    get_memory_info
    get_storage_info
    get_process_info
}

# Run the script
main
