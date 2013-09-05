using System;
using System.Globalization;

namespace CSharp
{
    public class Counter
    {
        int count;

        public Counter()
        {
            count = 0;
        }

        public void Increment()
        {
            count++;
        }

        public void Decrement()
        {
            count--;
        }

        public override string ToString()
        {
            return count.ToString(CultureInfo.CurrentUICulture);
        }

        public void Run()
        {
            var counter1 = new Counter();
            var counter2 = new Counter();

            counter1.Increment();
            counter1.Increment();
            counter1.Decrement();
            counter2.Decrement();
            counter2.Decrement();
            counter2.Decrement();
            counter1.Increment();

            Console.WriteLine("counter1: {0}", counter1);
            Console.WriteLine("counter2: {0}", counter2);
        }
    }
}
