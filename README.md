# config-manager

##Execution example

run

```bash
  python parse.py example.json
```


## Json domain structure example



```json
{
  "id":1,
  "domainName":"root",
  "tasks":[
    {
      "id":1,
      "name":"tache1",
      "priority":12,
      "function":"bidule",
      "stackSize":1000,
      "parameters":"NULL"
    },
    {
      "id":2,
      "name":"tache2",
      "priority":13,
      "function":"bidule2",
      "stackSize":2000,
      "parameters":"NULL"
    }
    ],
    "sub-partitions":[
    {
      "id":1,
      "name":"part1",
      "priority":12,
      "function":"bidulePart1",
      "stackSize":1000,
      "parameters":"NULL",
      "hw-access":["led1"],
      "queue-access":[1,2]
    },
    {
      "id":2,
      "name":"part2",
      "priority":13,
      "function":"bidulepart2",
      "stackSize":2000,
      "parameters":"NULL",
      "hw-access":["led2"],
      "queue-access":[1]

    }
    ],
    "hardware":[
    {
      "id":1,
      "hardware-name":"led1"
    },
    {
      "id":2,
      "hardware-name":"led2"
    }
    ],
    "queues":[]
}




```
