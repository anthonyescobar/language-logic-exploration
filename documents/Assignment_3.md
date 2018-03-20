# Homework 3

## Problem 7.1
```
// Use Euclid's algorithm to calculate the GCD.
private long GCD(long a, long b)
{
  a = Math.Abs(a);
  b = Math.Abs(b);

  for (; ; )
  {
    long remainder = a % b;
    if (remainder == 0) return b;
    a = b;
    b = remainder;
  };
}
```

## Problem 7.2

Bad comments may occur because the programmer isn't writing their code well enough to be read. In the case above, the programmer made comments basically line by line, which is not necessary. Most of he code is simple enough to be understood without comments due to the initial comment being explanitory, proper variable naming, and proper formatting.

## Problem 7.4

## Problem 7.5

It shouldn't be necessary to add error handling to the GCD code. It could be useful, however the data valdation would be better off in the calling function rather than in this function.

## Problem 7.7

How to get to the supermarket:
1. Get in car (and buckle seatbelt)
2. Turn on car engine
3. Exit parking spot and procede on the street in the direction of the supermarket
4. Enter parking lot of supermarket
5. Scan for parking closest to the entrance
6. Pull into parking spot
7. Get in car and enter supermarket

## Problem 8.1

To test an IsRelativelyPrime method it would be most appropriate to test numbers where the value of relatively prime is known ahead of time. Making another method that checks if two values are relatively prime would be a rehash of the code before and therefore unnessary.

## Problem 8.3

Because we don't know how IsRelativelyPrime works, the test would be black-box. An exhaustive test would be too much because of the range of values and permutations.

## Problem 8.5

## Problem 8.9

Exhustive tests can be considered black-box because they don't necessarily need to know what is going on in the code.

## Problem 8.11

1. Alice/Carmen = (5\*5)/2 = 12.5
2. Alice/Bob = (5\*4)/2 = 10
3. Bob/Carmen = (4\*5)/1 = 20
The Average of these values is 14 which means there are 14 bugs to fix

## Problem 8.12

The Lincoln estimate would be forced to divide by 0 if there are no bugs in common, causing an undefined result which is not a proper estimate of bugs. To get a proper lower bound, the tester can pretend that there was one bug in common between the testers.
