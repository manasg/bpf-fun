compile
```
g++ hello.cpp -o bin/hello && ./bin/hello 2 500
```

read binary
```
readelf -Ws bin/hello  | grep make_me_slow
```

demangle
```
nm -g --demangle bin/hello | grep make_me_slow
```

uprobe
```
bpftrace -e 'uprobe:bin/hello:make_me_slow {printf("ok\n");}'
```
