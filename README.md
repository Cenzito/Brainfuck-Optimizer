# Brainfuck-Optimizer
Coding of a Brainfuck Interpreter, Brainfuck Optimizer and Optimized Brainfuck Interpreter


## Report by Cenzo Poirier De Carvalho

# bf interpreter:
bfinterpret(code):
input: code in brainfuck (code)
output: (end pointer, end memory)
implementation: I used a memory of size 30000 to store the values. Then I added a pointer variable (mempointer) to store the value we are at in the memory. I also added a position variable (position) to store where we are in the code. Then while the code isn’t fully gone through we check each character one at a time and do whatever necessary depending on the character .,[]+- etc...
(.) prints out the value at the place where we are in the memory in ASCII equivalent code.
(,) asks for an integer input (between 0 and 256) and stocks it at the current place in memory. (+) increments the memory by 1 at the index indicated by the pointer
(-) increments the memory by 1 at the index indicated by the pointer
([) goes to the matching bracket ] if the value of the memory at the pointer is 0 else continues (]) goes to the matching bracket [ if the value of the memory at the pointer is not 0 else continues
(>) increments the pointer value by one
(<) decrements the pointer value by one
(note: the bracket matching is done by the brackmatch program and number of steps is implemented through using a counter and math.inf if no stepmax is given)
brackmatch(string):
input: string with sets of brackets
output: list with matching brackets
Implementation: Here I simply used the classic push/pop method to compute pairs of brackets. Example: brackmatch(‘+[++]’) returns [None,4,None,None,1]
# bf optimizer:
All Optimisations are implemented:
copy_multiply_loop_simplification(string):
input: bf code
output: optimized bf code with simpler loops
      
 Here I used the same format as postpone moves but with : and ; instead of () where [+>>-<<] is translated by ;2,-1;=0 which means that at an offset of 2, the memory will be decremented by one (256-memory[mempointer]) times. Then the memory at the current index is put to 0. [->>-<<] is translated by :2,-1:=0 which means that at an offset of 2, the memory will be decremented by one memory[mempointer] times. Then the memory at the current index is put to 0. I simply used postpone moves and some string manipulation to make this code work.
cancellation(string):
input: bf code
output: optimized bf code with simpler loops ([-] or [+] simply return =0 and [-]++ returns =2) This is essentially a particular case of the above where we simply set the pointed memory to 0 without any other modifications
scan(string):
Simply replaces very particular strings [>] and [<] using the replace function
inc_dec_fixed_offset(string):
Essentially postpone moves so I used it because I had already done it
postpone_moves(string):
Replaces ++>>--< by (0,2)(2,-2)>-1 just to simplify commands. Uses split which allows to split the string into parts that can and cannot be optimized then uses replace() to change what is in the optimizable strings.
contraction optimisations:
they simply turn - into +-1 -- into +-2 ++ into +2 and +-- into +-1. The same applies for pointer movements. >> becomes >2 < becomes >-1.
(note: they both use helper functions simarrowhelper and simplusfyhelper)
optimize(string):
Applies all previous optimizations in a particular order as to not mix certain commands up.
# bf optinterpreter:
Same core as interpret with a couple new commands as to use the optimized functions.
optinterpret(code):
input: optimized bf code
output: (mempointer,memory) (runs the code and gives memory and pointer) These commands have been added:
-(off,inc) increments the memory cell at an offset of off by inc.
Example: (2,2) increments the cell at mempointer+2 by 2
-;off,inc; means that at an offset of off, the memory will be incremented by inc (256-memory[mempointer]) times.
-:off,inc: means that at an offset of off, the memory will be incremented by inc memory[mempointer] times.
    
-=value means that the memory will be set to value
-|1| and |-1| now respectively search for the next and last empty cell of memory
