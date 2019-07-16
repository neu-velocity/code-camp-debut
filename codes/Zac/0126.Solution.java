class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> ans = new ArrayList();
        Map<String, List<String>> wcMap = new HashMap();
        for (String word : wordList) {
            for (int i = 0; i < word.length(); i++) {
                String wildcard = word.substring(0, i) + "*" + word.substring(i + 1);
                List<String> list = wcMap.getOrDefault(wildcard, new ArrayList());
                list.add(word);
                wcMap.put(wildcard, list);
            }
        }
        int len = beginWord.length();
        Set<String> visited = new HashSet();
        Queue<String> queue = new LinkedList();
        visited.add(beginWord);
        queue.add(beginWord);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<String> tmp = new ArrayList();
            while (size-- > 0) {
                String cur = queue.poll();
                String word = cur.substring(cur.length() - len);
                for (int i = 0; i < word.length(); i++) {
                    String wildcard = word.substring(0, i) + "*" + word.substring(i + 1);
                    if (visited.contains(wildcard)) {
                        continue;
                    }
                    tmp.add(wildcard);
                    for (String next : wcMap.getOrDefault(wildcard, new ArrayList<String>())) {
                        String seq = cur + "," + next;
                        if (next.equals(endWord)) {
                            ans.add(Arrays.asList(seq.split(",")));
                        } else if (!visited.contains(next)){
                            tmp.add(next);
                            queue.offer(seq);
                        }
                    }
                }
            }
            visited.addAll(tmp);
            if (!ans.isEmpty()) {
                break;
            }
        }
        return ans;
    }
}