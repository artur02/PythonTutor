using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharp
{
    public class Comprehension
    {
        public IEnumerable<int> nums;
        public List<int> numbers;
        public List<int> cubes;
        public List<int> cubesmod2;
        public Dictionary<int, int> cubesmod2dict;

        public Comprehension()
        {
            nums = Enumerable.Range(0, 100);

            // To list
            numbers = new List<int>(nums);

            // Cubes - Classical
            cubes = new List<int>();
            foreach (var number in nums)
            {
                cubes.Add(number*number*number);
            }

            // Cubes - Functional
            cubes = nums
                        .Select(x => x*x*x)
                        .ToList();

            // Cubes - even - Classical
            cubesmod2 = new List<int>();
            foreach (var number in nums)
            {
                var cube = number * number * number;
                if (cube % 2 == 0)
                {
                    cubesmod2.Add(cube);
                }
            }

            // Cubes - even - Functional
            cubesmod2 = nums
                            .Where(x => x % 2 == 0)
                            .Select(x => x * x * x)
                            .ToList();

            // Cube dictionary - even - Classical
            cubesmod2dict = new Dictionary<int, int>();
            foreach (var number in nums)
            {
                var cube = number * number * number;
                if (cube % 2 == 0)
                {
                    cubesmod2dict.Add(number, cube);
                }
            }

            // Cube dictionary - even - Functional
            cubesmod2dict = nums
                                .Where(x => x % 2 == 0)
                                .Select(x => new KeyValuePair<int, int>(x, x*x*x) )
                                .ToDictionary(x => x.Key, x => x.Value);
        }

        public void Run()
        {
            var comprehension = new Comprehension();

            Console.WriteLine("numbers:\n{0}", comprehension.numbers);
            Console.WriteLine("cubes:\n{0}", comprehension.cubes);
            Console.WriteLine("cubes even:\n{0}", comprehension.cubesmod2);
            Console.WriteLine("cubes even dictionary:\n{0}", comprehension.cubesmod2dict);
        }

        public void Run2()
        {
            var comprehension = new Comprehension();

            Console.WriteLine("numbers:\n{0}", string.Join(", ", comprehension.numbers));
            Console.WriteLine("cubes:\n{0}", string.Join(", ", comprehension.cubes));
            Console.WriteLine("cubes even:\n{0}", string.Join(", ", comprehension.cubesmod2));
            Console.WriteLine("cubes even dictionary:\n{0}", string.Join(", ", comprehension.cubesmod2dict));
        }

    }
}
