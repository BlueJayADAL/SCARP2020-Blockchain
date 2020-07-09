<h1> Hyperledger Fabric </h1>

<h2> Prerequisites:</h2>

Add to .bashrc:
<p><code>
export GOPATH=$HOME/go <p>
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
</code>
<p>
<code>
sudo systemctl enable docker
</code>
  
Add your user to the docker group:
<p><code>
sudo usermod -a -G docker $USER
</code><p>
Make sure the docker daemon is running:
<p><code>sudo systemctl start docker</code>

<h2>Install samples and binaries:</h2>
<p><code>curl -sSL https://bit.ly/2ysbOFE | bash -s -- 2.0.1 1.4.6 0.4.18</code>
<p><code>export PATH=<path to download location>/bin:$PATH</code>

<h3>Test network:</h3>
<p><code>cd fabric-samples/test-network</code>
<p>Make sure network is down:
<p><code>./network.sh down</code>
<p>Bring network up:
<p><code>./network.sh up</code>
<p>Create channel “mychannel”:
<p><code>./network.sh createChannel</code>
<p>Start chaincode on channel:
<p><code>./network.sh deployCC</code>
<p>Add peer binaries to $PATH:
<p><code>export PATH=${PWD}/../bin:${PWD}:$PATH</code>
<p>Add path to fabric-samples and core.yaml:
<p><code>export FABRIC_CFG_PATH=$PWD/../config/</code>
<p>Add environment variables to Org1:
<p><code>export CORE_PEER_TLS_ENABLED=true</code>
<p><code>export CORE_PEER_LOCALMSPID="Org1MSP"</code>
<p><code>export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt</code>
<p><code>export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp</code>
<p><code>export CORE_PEER_ADDRESS=localhost:7051</code>
<p>Query car ledger:
<p><code>peer chaincode query -C mychannel -n fabcar -c '{"Args":["queryAllCars"]}'</code>
<p>Change owner of car:
<p><code>peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n fabcar --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"changeCarOwner","Args":["CAR9","Dave"]}'</code>
<p>Add environment variables to Org2:
<p><code>export CORE_PEER_TLS_ENABLED=true</code>
<p><code>export CORE_PEER_LOCALMSPID="Org2MSP"</code>
<p><code>export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt</code>
<p><code>export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp</code>
<p><code>export CORE_PEER_ADDRESS=localhost:9051</code>
<p>Query Org2 chaincode:
<p><code>peer chaincode query -C mychannel -n fabcar -c '{"Args":["queryCar","CAR9"]}'</code>
<p>Bring the network down:
<code>./network.sh down</code>

Bring up the network with Certificate Authorities:

cd fabric-samples/test-network

Make sure network is down:
./network.sh down

Bring up network with CA flag:
./network.sh up -ca

Examine MSP structure:
tree organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/

Bring the network down:
./network.sh down

Deploying a Smart Contract to a channel:

cd fabric-samples/test-network

./network.sh down

./network.sh up createChannel

-Setup Logspout:

-copy script to current directory:
cp ../commercial-paper/organization/digibank/configuration/cli/monitordocker.sh .


-start Logspout:
./monitordocker.sh net_test

-Package Smart Contract:
-open new terminal window

-install chaincode dependenceis:
cd fabric-samples/chaincode/fabcar/javascript

npm install

cd ../../../test-network

-add peer binaries to $PATH
export PATH=${PWD}/../bin:${PWD}:$PATH

-add core.yaml to $PATH:
export FABRIC_CFG_PATH=$PWD/../config/

-confirm installed correctly:
peer version

-establish Org1 admin as identity:
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp

-create chaincode package:
peer lifecycle chaincode package fabcar.tar.gz --path ../chaincode/fabcar/javascript/ --lang node --label fabcar_1

-install package on peers:

-set environment variables to operate peer CLI as Org1 admin:
export CORE_PEER_TLS_ENABLED=true
export CORE_PEER_LOCALMSPID="Org1MSP"
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export CORE_PEER_ADDRESS=localhost:7051

-install chaincode:
peer lifecycle chaincode install fabcar.tar.gz

-same process for Org2:
export CORE_PEER_LOCALMSPID="Org2MSP"
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
export CORE_PEER_ADDRESS=localhost:9051
-approve chaincode definition:
peer lifecycle chaincode queryinstalled

-save package id as path variable (replace your package id with the one below):
CC_PACKAGE_ID=fabcar_1:69de748301770f6ef64b42aa6bb6cb291df20aa39542c3ef94008615704007f3

-approve the chaincode:
peer lifecycle chaincode approveformyorg -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --channelID mychannel --name fabcar --version 1.0 --package-id $CC_PACKAGE_ID --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem

-set Org1 as admin and approve chaincode definition:
export CORE_PEER_LOCALMSPID="Org1MSP"
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export CORE_PEER_ADDRESS=localhost:7051
peer lifecycle chaincode approveformyorg -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --channelID mychannel --name fabcar --version 1.0 --package-id $CC_PACKAGE_ID --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem

-check if peers have approved chaincode definition:
peer lifecycle chaincode checkcommitreadiness --channelID mychannel --name fabcar --version 1.0 --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem --output json

-commit chaincode definition to channel:
peer lifecycle chaincode commit -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --channelID mychannel --name fabcar --version 1.0 --sequence 1 --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt

-confirm the chaincode has been committed:
peer lifecycle chaincode querycommitted --channelID mychannel --name fabcar --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem

-invoke the chaincode:
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n fabcar --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"initLedger","Args":[]}'

-query the ledger:
peer chaincode query -C mychannel -n fabcar -c '{"Args":["queryAllCars"]}'

-upgrade a deployed chaincode:
************************SKIPPED FOR NOW******************************

-clean up the network:
docker stop logspout
docker rm logspout















WRITING AN APPLICATION:
https://hyperledger-fabric.readthedocs.io/en/release-2.0/write_first_app.html

-install build essentials if you haven’t done so:
sudo apt install build-essential

cd fabric-samples/fabcar
./startFabric.sh javascript
cd javascript
npm install

-enroll admin user:
node enrollAdmin.js

-register and enroll application user:
node registerUser.js

-query ledger:
node query.js

-change chaincode transaction request:
cd fabric-samples/chaincode/fabcar/javascript/lib
-open query.js in text editor
-change line 44 to:
const result = await contract.evaluateTransaction('queryCar', 'CAR4');
-navigate back to fabcar/javascript and run query.js:
node query.js

-update the ledger:
-open invoke.js in text editor
-change line 43 to the below and save:
await contract.submitTransaction('createCar', 'CAR12', 'Honda', 'Accord', 'Black', 'Tom');
-run invoke.js
node invoke.js
-to see that the transaction has taken place open query.js in text editor and change line 44 to below and save:
const result = await contract.evaluateTransaction('queryCar', 'CAR12');
-run query.js
node query.js
-to change a car’s owner, open invoke.js in text editor and change line 43 to below and save:
await contract.submitTransaction('changeCarOwner', 'CAR12', 'Dave');
-run invoke.js:
node invoke.js
-query result:
node query.js

-shutdown network:
cd ..
./networkDown.sh

