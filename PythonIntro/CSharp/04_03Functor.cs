using System;
using System.Collections;
using System.Collections.Generic;

namespace CSharp
{
    public interface ICallable
    {
        bool Call(int operand1, int operand2);
    }

    public enum Direction
    {
        Up = 0,
        Down = 1
    }

    public class IntComparator : ICallable
    {
        readonly Direction dir;

        public IntComparator(Direction dir = Direction.Up)
        {
            this.dir = dir;
        }

        public bool Call(int operand1, int operand2)
        {
            switch (dir)
            {
                case Direction.Up:
                    return operand1 < operand2;
                case Direction.Down:
                    return operand1 > operand2;
                default:
                    throw new NotSupportedException();
            }
        }
    }

    public class Sorter
    {
        readonly IList items;
        readonly IntComparator comp;

        public Sorter(IList items, IntComparator comparator)
        {
            this.items = items;
            comp = comparator;
        }

        public IList Sort()
        {
            for (int i = 0; i < items.Count; i++)
            {
                var valueToInsert = (int)items[i];
                var holePos = i;
                while (holePos > 0 && comp.Call(valueToInsert, (int)items[holePos-1]))
                {
                    items[holePos] = items[holePos - 1];
                    holePos--;
                    items[holePos] = valueToInsert;
                }
            }

            return items;
        }
    }

    public class SortRunner
    {
        public void Run()
        {
            var items = new List<int>() { 3, 7, 4, 9, 5, 2, 6, 1 };
            Console.WriteLine("items: \t\t{0}", string.Join(", ", items));

            var sorter = new Sorter(items, new IntComparator());
            var result = sorter.Sort() as List<int>;
            Console.WriteLine("items up: \t{0}", string.Join(", ", result));

            var sorter2 = new Sorter(items, new IntComparator(Direction.Down));
            var result2 = sorter2.Sort() as List<int>;
            Console.WriteLine("items down: \t{0}", string.Join(", ", result2));
        }
    }
}
