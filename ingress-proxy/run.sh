echo test
socat tcp-listen:8099,reuseaddr,fork tcp:192.168.0.10:80
