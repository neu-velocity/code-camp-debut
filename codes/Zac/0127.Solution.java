class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Map<String, List<String>> map =  new HashMap();
        for (String word : wordList) {
            for (int i = 0; i < word.length(); i++) {
                String wildcard = word.substring(0, i) + "*" + word.substring(i + 1);
                List<String> list = map.getOrDefault(wildcard, new ArrayList());
                list.add(word);
                map.put(wildcard, list);
            }
        }
        Set<String> visited = new HashSet();
        Queue<String> queue = new LinkedList();
        visited.add(beginWord);
        queue.offer(beginWord);
        int len = 1;
        while (!queue.isEmpty()) {
            len++;
            int size = queue.size();
            while (size-- > 0) {
                String word = queue.poll();
                for (int i = 0; i < word.length(); i++) {
                    String wildcard = word.substring(0, i) + "*" + word.substring(i + 1);
                    if (visited.contains(wildcard)) {
                        continue;
                    }
                    visited.add(wildcard);
                    for (String next : map.getOrDefault(wildcard, new ArrayList<String>())) {
                        if (visited.contains(next)) {
                            continue;
                        }
                        visited.add(next);
                        queue.offer(next);
                    }
                }
            }
            if (visited.contains(endWord)) {
                return len;
            }
        }
        return 0;
    }
}