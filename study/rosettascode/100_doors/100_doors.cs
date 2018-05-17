/*namespace doors
{
    class doors
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello world!");
        }
    }
}*/

// unoptimized

namespace ConsoleApplication1
{
    using System;
    class Program
    {
        static void Main(string[] args)
        {
            bool[] doors = new bool[100];
 
            //Close all doors to start.
            for (int d = 0; d < 100; d++) doors[d] = false;
 
            //For each pass...
            for (int p = 0; p < 100; p++)//number of passes
            {
                //For each door to toggle...
                for (int d = 0; d < 100; d++)//door number
                {
                    if ((d + 1) % (p + 1) == 0)
                    {
                        doors[d] = !doors[d];
                    }
                }
            }
 
            //Output the results.
            Console.WriteLine("Passes Completed!!!  Here are the results: \r\n");
            for (int d = 0; d < 100; d++)
            {
                if (doors[d])
                {
                    Console.WriteLine(String.Format("Door #{0}: Open", d + 1));
                }
                else
                {
                    Console.WriteLine(String.Format("Door #{0}: Closed", d + 1));
                }
            }
            Console.ReadKey(true);
        }
    }
}


// optimized

/*namespace ConsoleApplication1
{
    using System;
    class Program
    {
        static void Main()
        {
            //The o variable stores the number of the next OPEN door.
            int o = 1;
            int f = 1;
            int l = 5;
            Random r = new Random();
            o = r.Next(f, l);
 
            //The d variable determines the door to be output next.
            for (int d = 1; d <= 100; d++)
            {
                Console.Write("Door #{0}: ", d);
                if (d == o)
                {
                    Console.WriteLine("Open");
                    f = f + 5;
                    l = l + 5;
                    o = r.Next(f, l);
                }
                else
                    Console.WriteLine("Closed");
            }
            Console.ReadKey(true);
        }
    }
}*/


