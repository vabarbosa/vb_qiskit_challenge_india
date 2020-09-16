# the write_and_run function writes the content in this cell into the file "feature_map.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, PauliFeatureMap
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def feature_map(): 
    # BUILD FEATURE MAP HERE - START
    
    # import required qiskit libraries if additional libraries are required
    
    # build the feature map
    feature_map = ZZFeatureMap(feature_dimension=3, reps=5, insert_barriers=True)
    
    # BUILD FEATURE MAP HERE - END
    
    #return the feature map which is either a FeatureMap or QuantumCircuit object
    return feature_map
# the write_and_run function writes the content in this cell into the file "variational_circuit.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import  RealAmplitudes, EfficientSU2
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def variational_circuit():
    # BUILD VARIATIONAL CIRCUIT HERE - START
    
    # import required qiskit libraries if additional libraries are required
    
    # build the variational circuit
    var_circuit = EfficientSU2(3, reps=5)

    # BUILD VARIATIONAL CIRCUIT HERE - END
    
    # return the variational circuit which is either a VaritionalForm or QuantumCircuit object
    return var_circuit
# # the write_and_run function writes the content in this cell into the file "optimal_params.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def return_optimal_params():
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    
    optimal_parameters = [ 1.4938224 ,  0.7722673 ,  0.04673808, -0.40266667, -0.71464356,
       -1.01611661,  0.95701616, -0.11231763, -0.11372508, -1.66516913,
        0.34996265, -0.3358157 ,  1.23830127, -0.08761782,  2.15049145,
       -0.10287426,  0.01249375,  0.39226141, -0.31795359, -2.51407333,
        1.84024971, -0.43272372, -0.99526383,  1.86503194,  0.19557005,
        1.01820773,  0.58771594,  2.10347774, -2.01914662,  1.12136122,
       -0.08569531,  0.31626583, -0.59179025, -2.03737758, -0.30077671,
       -1.13613034]
    
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    return np.array(optimal_parameters)
