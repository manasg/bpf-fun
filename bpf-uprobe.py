#!/usr/local/bin/python3
from bcc import BPF

program = r"""

void static loop() {
    u64 sleep_ns = 5;
    u64 start = bpf_ktime_get_ns();
    u64 now = start;

    while(now < (start + sleep_ns)) {
        now = bpf_ktime_get_ns();
    }
}

int hello(void *ctx) {
    bpf_trace_printk("hii");
    loop();
    return 0;
}
"""

b = BPF(text=program)
b.attach_uprobe(name="bin/hello", sym_re=".*make_me_slow.*", fn_name="hello")

b.trace_print()
