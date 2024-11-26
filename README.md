# navCSP test: Subset Sum

```
class Obj { ref : 0-* reference, attribute : int}

Context Obj inv:
  let query = self.ref.ref.....ref in
    query->sum(attribute) = Target and
    query->isUnique(attribute)
```

## Dimensions:
- n : number of pointers to model ref
- r : query depth
- objects : number of elements in the multiset
- multi : number of different elements in the multiset
- first : first value of the multiset
- target : target sum of the problem

## Compilation & exécution
```bash
# build
./gradlew build

# run
./gradlew run
```
## the Multiset
- if `multi=4` and `first=10` the multiset will look like \{10,11,12,13,10,11,..\} repeating
- if `objects=5` and the above, the multiset will be \{10,11,12,13,10\}
- if `target=33` \{10,13\} would be a solution, if `target=0` \{\} is a solution, this multiset can't sum up to `target=1`

## the paths to SubSets
Finding a solution in our context means finding a path of n steps, from the first element, to a subset fitting the constraints.

![subsetsumpath](readme/subsetsumpath.png)

In the image, any number of steps from 10 reaches a subset summing to 33.
To take a step, one follows all the outgoing arrows from the current collection of objects.
From \{10\} we reach \{11,12\} in one step, from \{11,12\} we reach \{10,13\} in one step, and from \{10,13\} we step back to \{11,12\}.