
# Improving segmentation and clustering in a speaker diarization pipeline


## Installations Guide
1. Install an environment manager. Recommeneded:[anaconda](https://www.anaconda.com/)
```bash
conda create -n VBx python=3.6
conda activate VBx
```
2. Clone the repo:
```bash
git clone https://github.com/Lee-Fingerhut/Improving-segmentation-and-clustering-in-a-speaker-diarization-pipeline.git
```
3. Install the package
```bash
pip install -e .
```
4. Initialize submodule `dscore`:
```bash
git submodule init
git submodule update
```
## Predicting
Predicting for a test wav file:
```bash
./run.sh $(filename).wav
```

## Credit
Federico Landini, J ́an Profant, Mireia Diez, Luk ́aˇs Burget

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



