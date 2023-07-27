#!/usr/local/bin/python3
from bcc import BPF

program = r"""

struct data {
	int x;
};


static int empty_callback(__u32 index, void *something) {
	return 0;
}

int hello(void *ctx) {
    struct data d = {};
    d.x = 1;

    u32 loops = 2;
    u32 nr_loops_returned = 0;
    
    bpf_trace_printk("hii");
    nr_loops_returned = bpf_loop(loops, empty_callback, &d, 0);
    return 0;
}
"""

b = BPF(text=program)
b.attach_uprobe(name="bin/hello", sym_re=".*make_me_slow.*", fn_name="hello")

b.trace_print()
