class Solution {
    private static final Map<Character, Character> BRACKET_MAP = new HashMap<>();
    static {
        BRACKET_MAP.put(')', '(');
        BRACKET_MAP.put(']', '[');
        BRACKET_MAP.put('}', '{');
    }
        
    public boolean isValid(String s) {

        
        Deque<Character> myStack = new ArrayDeque<>();

        //Every open ( [, (, { ) followed by a Close ( ], ), } )
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[' ||
                s.charAt(i) == '{' ||
                s.charAt(i) == '(' ) {
                    myStack.push(s.charAt(i));
                }
            else {
                if (BRACKET_MAP.get(s.charAt(i)) == myStack.peek()) {
                    myStack.pop();
                } else {
                    return false;
                }
            }
        }

        return myStack.isEmpty();
    }
}
