# Endurance-Aware Compiler for 3-D Stackable FeRAM as Global Buffer in TPU-Like Architecture

Problem: 
*   Looking for new technologies that offer low leakge power and high memory density compared to SRAM and eDRAM (expensive refresh power).
*   The new technologies suffer from limited endurance cycles.

Prototype: Intel's prototype 3D stackable ferrorelectric random access memory (FeRAM)  is considered as the global
buffer memory of a tensor-processing-unit (TPU)-like architecture.

Solution: 
*   An endurance-aware compiler to evaluate the maximum number of DNN trainings wrt to the endurance limit.
*   Wear leveling
*   Dual-mode operation - voaltile and non-volatile.

Advantages of FeRAM:
*   Non-volatile → almost zero leakage
*   High density, especially with 3-D stacking
*   Fast read/write (~2 ns)

Limitations of FeRAM:
*   FeRAM consumes high read and write energy with relatively higher operating voltage than that of core logic.
*   Limited cycling endurance which is consumed by both read and write operations.  10^10 and 10^15
*   Read-destructive nature where an active write-back operation is required after every read operation. 

*The paper asks: Can FeRAM realistically be used as the global buffer in a TPU for DNN training?*

Contributions of this paper:
*   Comparison of FeRAM as a global buffer of a TPU-like architecture for DNN training compared to SRAM and eDRAM.
*   A runtime reconfigurable endurance aware compiler is developed that can use wear leveling and dual mode techniques to increase the lifetime of the 