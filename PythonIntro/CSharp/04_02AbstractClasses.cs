using System;

namespace CSharp
{
    public interface IAnimal
    {
        string GetAvgWeight();
    }

    public interface ITalker
    {
        string Talk();
    }

    public class Duck : IAnimal, ITalker
    {
        public string GetAvgWeight()
        {
            return "10kg";
        }

        public string Talk()
        {
            return "Quack";
        }

        public void Run()
        {
            var duck = new Duck();
            Console.WriteLine("Duck average weight: {0}", duck.GetAvgWeight());
            Console.WriteLine("Duck talks: {0}", duck.Talk());
        }
    }

}
