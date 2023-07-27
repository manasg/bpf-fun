#!/usr/local/bin/python3
from bcc import BPF

program = r"""


struct callback_ctx {
    int output;
};

u32 nested_callback_nr_loops;
u32 stop_index = -1;

int nr_loops_returned;
int g_output;
int err;

static int empty_callback(__u32 index, void *data)
{
	return 0;
}

int hello(void *ctx) {
    bpf_trace_printk("hii");
    u32 nr_loops = 3;
    nr_loops_returned = bpf_loop(nr_loops, empty_callback, NULL, 0);
    return 0;
}
"""

b = BPF(text=program)
b.attach_uprobe(name="bin/hello", sym_re=".*make_me_slow.*", fn_name="hello")

b.trace_print()
