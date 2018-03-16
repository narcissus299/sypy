import sys
sys.path.append("./sypy")

import sypy

sybil_region = sypy.Region(
    graph=sypy.CompleteGraph(num_nodes=100),
    name="SybilCompleteGraph", 
    is_sybil=True
)

honest_region = sypy.Region(
    graph=sypy.SmallWorldGraph(
        num_nodes=5000,
        node_degree=100,
        rewire_prob=0.8
    ),
    name="HonestSmallWorldGraph"
)
honest_region.pick_random_honest_nodes(num_nodes=10)

social_network = sypy.Network(
    left_region=honest_region,
    right_region=sybil_region,
    name="OnlineSocialNetwork"
)
social_network.random_pair_stitch(num_edges=10)

detector = sypy.SybilTrustDetector(social_network)
results = detector.detect()

print("accuracy={0:.2f}, sensitivity={1:.2f}, specificity={2:.2f}".format(
    results.accuracy(),
    results.sensitivity(),
    results.specificity()
))