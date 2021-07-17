EBNF:

expr = expr + expr;
expr = expr - expr;
expr = expr * expr;
expr = expr / expr;
expr = DIGIT | expr;
DIGIT = 0|1|2|3|4|5|6|7|8|9

Explanation:
Rules are explored in the same order.
Why it is important because of precedence.
We cannot by pass the rules.

STEP-1:
Parser will generate the AST.


STEP-2:
AST will generate the assembly

STEP-3:
Assembly will be converted to exe.

We will skip step2 and step3 and will evaluate the expression directly.


