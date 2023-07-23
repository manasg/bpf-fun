compile
```
g++ hello.cpp -o bin/hello && ./bin/hello 2 500
```

read binary
```
readelf -Ws bin/hello  | grep critical
```

demangle
```
nm -g --demangle bin/hello | grep critical
```

uprobe
```
bpftrace -e 'uprobe:bin/hello:critical {printf("ok\n");}'
```
