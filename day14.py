from dataclasses import dataclass
d = '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''

d = open('inputs/14.txt').read()

@dataclass
class deer():
    name:str
    speed:int
    rest_time: int 
    distance:int = 0 
    total_distance:int = 0 
    fly_time: int = 0 
    points : int = 0
    
pack: list[deer] = []
for line in d.splitlines():
    out = line.split(' ')
    speed = int(out[3])
    rest_time = int(out[-2])
    max_t = int(out[6])
    name = out[0]

    pack.append(deer(name=name,speed=speed,rest_time=rest_time,fly_time=max_t))

print(pack)
ttime = 2503

for d in pack:
   d.distance = d.fly_time * d.speed
   rem = ttime % (d.fly_time + d.rest_time)
   d.total_distance = ttime//(d.fly_time + d.rest_time) * d.distance + d.speed * min(rem,d.fly_time)

ps = sorted(pack,key=lambda x:x.total_distance,reverse=True)
print(ps[0].name, ps[0].total_distance)

# part 2

ttime = 2503
for t in range(0,ttime+1):
    for d in pack:
        d.distance = d.fly_time * d.speed
        rem = t % (d.fly_time + d.rest_time)
        d.total_distance = t//(d.fly_time + d.rest_time) * d.distance + d.speed * min(rem,d.fly_time)
    # top ones get a point
    top_dist = max([d.total_distance for d in pack])
    if t>0:
        for d in pack:
            if d.total_distance == top_dist:
                d.points+=1

ps = sorted(pack,key=lambda x:x.points,reverse=True)
print(ps[0].name, ps[0].points)
