class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;

        while (l < r) {
            char left = s.charAt(l);
            char right = s.charAt(r);

            // Skip non-alphanumeric characters
            if (!Character.isLetterOrDigit(left)) {
                l++;
                continue;
            }
            if (!Character.isLetterOrDigit(right)) {
                r--;
                continue;
            }

            // Compare ignoring case
            if (Character.toLowerCase(left) != Character.toLowerCase(right)) {
                return false;
            }

            l++;
            r--;
        }

        return true;

    }
}
