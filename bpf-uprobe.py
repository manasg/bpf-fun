#!/usr/local/bin/python3
from bcc import BPF

program = r"""

struct callback_ctx {
	int output;
};


static int empty_callback(__u32 index, void *data) {
	return 0;
}

int hello(void *ctx) {
    struct callback_ctx data = {};
    u32 loops = 2;
    u32 nr_loops_returned = 0;
    
    bpf_trace_printk("hii");
    nr_loops_returned = bpf_loop(loops, empty_callback, NULL, 0);
    return 0;
}
"""

b = BPF(text=program)
b.attach_uprobe(name="bin/hello", sym_re=".*make_me_slow.*", fn_name="hello")

b.trace_print()
