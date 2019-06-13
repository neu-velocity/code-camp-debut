class Solution {

    enum Type { ENTER, LEAVE }

    class Event implements Comparable<Event> {

        Type type;
        int x, y;

        Event(int x, int y, Type type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }

        @Override
        public int compareTo(Event e) {
            if (this.x != e.x) {
                return this.x - e.x;
            } else if (this.type != e.type) {
                // process ENTER first
                if (this.type == Type.ENTER) {
                    return -1;
                } else {
                    return 1;
                }
            } else {
                if (this.type == Type.ENTER) {
                    // higher first
                    return e.y - this.y;
                } else {
                    // lower first
                    return this.y - e.y;
                }
            }
        }
    }

    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> points = new ArrayList();
        List<Event> eventList = new ArrayList();
        for (int[] b : buildings) {
            eventList.add(new Event(b[0], b[2], Type.ENTER));
            eventList.add(new Event(b[1], b[2], Type.LEAVE));
        }
        Collections.sort(eventList);
        PriorityQueue<Integer> maxHeap = new PriorityQueue(Collections.reverseOrder());
        maxHeap.offer(0);
        for (Event e : eventList) {
            if (e.type == Type.ENTER) {
                if (e.y > maxHeap.peek()) {
                    List<Integer> p = new ArrayList();
                    p.add(e.x);
                    p.add(e.y);
                    points.add(p);
                }
                maxHeap.offer(e.y);
            } else {
                maxHeap.remove(e.y);
                if (e.y > maxHeap.peek()) {
                    List<Integer> p = new ArrayList();
                    p.add(e.x);
                    p.add(maxHeap.peek());
                    points.add(p);
                }
            }
        }
        return points;
    }
}