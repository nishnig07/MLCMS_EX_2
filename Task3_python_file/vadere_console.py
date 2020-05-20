import json
import os

path = './TestOSM_Copy/scenarios/rimea_06_corner.scenario'
with open(path) as file:
    data = json.load(file)

scenario = data['scenario']
topgraphy = scenario['topography']
dynamic_elements = topgraphy['dynamicElements']

pedestrian = {
  "source" : None,
  "targetIds" : [ 1],
  "position" : {
    "x" : 12.3,
    "y" : 1.9
  },
  "velocity" : {
    "x" : 0.0,
    "y" : 0.0
  },
  "nextTargetListIndex" : 0,
  "freeFlowSpeed" : 1.3517178674547023,
  "attributes" : {
    "id" : -1,
    "radius" : 0.2,
    "densityDependentSpeed" : False,
    "speedDistributionMean" : 1.34,
    "speedDistributionStandardDeviation" : 0.26,
    "minimumSpeed" : 0.5,
    "maximumSpeed" : 2.2,
    "acceleration" : 2.0,
    "footStepsToStore" : 4,
    "searchRadius" : 1.0,
    "angleCalculationType" : "USE_CENTER",
    "targetOrientationAngleThreshold" : 45.0
  },
  "idAsTarget" : -1,
  "isChild" : False,
  "isLikelyInjured" : False,
  "mostImportantEvent" : None,
  "salientBehavior" : "TARGET_ORIENTED",
  "groupIds" : [ ],
  "trajectory" : {
    "footSteps" : [ ]
  },
  "groupSizes" : [ ],
  "modelPedestrianMap" : { },
  "type" : "PEDESTRIAN"
}
dynamic_elements += [pedestrian]
data['scenario']['topography']['dynamicElements'] = dynamic_elements
data['name'] = "rimea06_corner_task3"
# Serializing json
json_object = json.dumps(data, indent=4)

# Writing as .scenario file
with open("rimea06_corner_task3.scenario", "w") as outfile:
  outfile.write(json_object)

os.system('java -jar vadere-console.jar scenario-run --scenario-file "./rimea06_corner_task3.scenario" --output-dir="./output"')
