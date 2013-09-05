using System;

namespace CSharp
{
    public class Tuples
    {
        public Tuple<int, int, int> point;

        public Tuples()
        {
            point = Tuple.Create(1, 2, 3);
        }

        public void Run()
        {
            var tuples = new Tuples();
            Console.WriteLine(tuples.point);

            var x = tuples.point.Item1;
            var y = tuples.point.Item2;
            var z = tuples.point.Item3;

            Console.WriteLine("Point[x: {0}; y: {1}; z:{2}]", x, y, z);
        }
    }
}
