# Call Stack (Understanding Recursion)
* When you call a function, they system sets aside space in memory for that function to do its necessary work.
    * We frequently call such chuncks of memory **stack frames** or **function frames**.
* More than one function's stack frame may exist in memory at a given time. If main() calls move(), which then calls direction(), all three functions have open frames.
---
* These frames are arranged in a **stack**. **The frame for the most-recently called function in always on the top of the stack.**
* When a new function is called, a new frame is **pushed** onto the top of the stack and becomes the active frame.
* When a function finishes its work, its frame is **pooped** off of the stack, and the frame is immediately below it becomes the new, active, function on the top of the stack. This function picks up immediately where it left off.