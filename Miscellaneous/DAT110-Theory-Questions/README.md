## Oppgave 1 (10%)
**Q: What is Internetworking and the Internet about?**

<details>
<summary>Answer</summary>

Enabling a network of networks comprised of a heterogenous collection of network technologies
</details>

**Q: In the basic Internet network model, where are applications residing?**
1) In the network edge 
2) Typically run as processes on different computers and communicating over a network 
3) More reliable and more scalable than conventional applications
<details>
<summary>Answer</summary>
2 is correct
 
</details>

**Q: Transmission delay and propagation delay at a node(host or packet switch) are related?**

<details>
<summary>Answer</summary>

False
</details>

**Q: What is traffic intensity a measure of?**

<details>
<summary>Answer</summary>

A relation between amount of bits received per time unit for transmission on the communication link DNand the rate with which the bits can be transmitted.
</details>

**Q: Which of the following situations may lead to loss of datagrams / packets in a packet-switched network?**


1) There may be some intereference on a communication link causing some of the transmitted bits to be changed. 
2) Some buffers may overflow because too many packets arrive for a transmission on a communication link.

**Q: Which of the following is not a layer in the TCP/IP protocol stack?**

<details>
<summary>Answer</summary>

Session
</details>

**Q: A service provided by a layer also mandates the protocol that must be used to implement the service?**

<details>
<summary>Answer</summary>

False
</details>

**Q: What layers of the TCP/IP protocol stack does a router implement?**

<details>
<summary>Answer</summary>

Physical, Link, Network
</details>

**Q: Which of the following protocols belong to the application layer of the TCP/IP protocol stack?**

<details>
<summary>Answer</summary>

DNS, HTTP
</details>

**Q: What service does the TCP/IP network layer provide?**

<details>
<summary>Answer</summary>

Unreliable multi-hop communication of datagrams between endpoints also: Unrealiable multi-hop forwarding of datagrams between hosts.
</details>

**Q: Assume that a router is connecting to three different communication links. How many instances of the link layer would the router have?**

<details>
<summary>Answer</summary>

3
</details>

**Q: What is the IP address 10011110001110010100011001111010 (32-bit) written in dotted decimal notation?**

<details>
<summary>Answer</summary>

158.57.70.122
</details>

**Q: What 48-bit pattern does the link-layer address 50:7B:9D:E7:19:D0 correspond to?**

<details>
<summary>Answer</summary>

010100000111101110011101111001110001100111010000
</details>

**Q: How are communication end-points identified at the transport layer of the TCP/IP protocol stack?**

<details>
<summary>Answer</summary>

Using Ip addresses and port numbers.
</details>

**Q: What is the main purpose of the Socket API provided via the operating system?**

<details>
<summary>Answer</summary>

Makes it possible for application developers to access the TCP and UDP transport services.
</details>

**Q: What service does the UDP protocol provide?**

<details>
<summary>Answer</summary>

Unrealible end-to-end transmission of datagrams between hosts.
</details>

**Q: What service does the TCP protocol provide?**

<details>
<summary>Answer</summary>

Reliable bidirectional transmission of byte-streams between hosts.
</details>

**Q: All running processes constituting a networked and distributed application must be implemented in the same programming language?**

<details>
<summary>Answer</summary>

False
</details>

**Q: Which of the following method/operations does the HTTP protocol support?**

<details>
<summary>Answer</summary>

1.DELETE 2.POST 3.PUT 4.GET
</details>

**Q: What is the main purpose of the Domain Name System (DNS) ?**

<details>
<summary>Answer</summary>

Mapping of hostnames to IP addresses.
</details>

<details>
<summary>Answer</summary>

1. Handle applications heterogeneity in a message queue system 2.Can route messages to consumers that subscribed to a particular topic 3. Transforms incoming messages to target format
</details>

<details>
<summary>Answer</summary>

Pipelining pattern
</details>

<details>
<summary>Answer</summary>

True
</details>

<details>
<summary>Answer</summary>

1. Processes can use the overlay network to route messages to other processes in the overlay 2. Overlay network may span several physical networks
</details>

<details>
<summary>Answer</summary>

1. The overlay network has a delay cost to route messages between the two nodes that is twice the delay cost of the underlying network.
</details>

<details>
<summary>Answer</summary>

1. Messages will be routed through every connected node in the network. 2. The number of messages routed always depends on the number of edges(paths) in the overlay network.
</details>

**Q: An application-layer overlay network has 10000 replicated nodes, about 99% of these nodes have received update. You have developed an algorithm that keeps track of this statistic in the network. Which operation would be best to prioritize to get the remaining 1% nodes updates?**

<details>
<summary>Answer</summary>

Push-pull
</details>

**Q: Asynchronous RPC can be implemented by using the concept of?**

<details>
<summary>Answer</summary>

1.Callback that triggers a function at the client’s end 2. Multi-threading
</details>

<details>
<summary>Answer</summary>

Reduce the number of messages in the network.
</details>

<details>
<summary>Answer</summary>

1.Push-Pull (Nodes P and Q send updates to each other) 2. Pull(Node P, pulls new updates from node Q) 3. Push(Node P only pushes its own updates to node Q)
</details>

**Q: An unstructured p2p overlay network of 500 has nodes has a probabiliyt ( p =0.6) that two nodes are connected by an edge. What is the estimated number of messages that can be routed in this network?**

<details>
<summary>Answer</summary>

75000
</details>

**Q: An unstructured p2p overlay network of 500 nodes has a probability (p = 0.4) that two nodes are connected by an edge. What is the estimated number of messages that can be routed in this network?**

<details>
<summary>Answer</summary>

50000
</details>

**Q: Consider a tree and a fully connected overlay network with 10 nodes each. What is the total number of messages that will be routed across both topologies using flooding-based multicasting?**

<details>
<summary>Answer</summary>

9 messages in the tree and 45 messages in the fully-connected network.
</details>

<details>
<summary>Answer</summary>

1. Availability 2. Fault-tolerance 3. Scalability
</details>

<details>
<summary>Answer</summary>

Poor geographical scalability
</details>

<details>
<summary>Answer</summary>

1. Replicating higher level DNS servers 2. Caching at the local DNS servers
</details>

<details>
<summary>Answer</summary>

1.In recursive resolution, communication distance may not be an issue. 2. In iterative resolution, communication latency can be an issue 3. In recursive resolution, higher-level servers may have too much load.
</details>

<details>
<summary>Answer</summary>

All valid names recognized and managed by a service.
</details>

**Q: You are tasked to design a lookup for a chord system that can scale, which lookup algorithm would you recommend?**

<details>
<summary>Answer</summary>

An approach where each node can use a routing table containing references to a few expotentionally distant nodes.
</details>

**Q: The Domain Name System(DNS) is used to map the hostname to the IP address. Which statements are correct?**

<details>
<summary>Answer</summary>

1. The DNS Is hierarchically organized where the root node is contacted to start the name resolution. 2. An authorative name server is the server that stores and provides the actual IP address of the hostname of the local DNS server.
</details>

**Q: A Distributed Hash Table uses 8bits to define its addres space. What is the size of the address in this space?**

<details>
<summary>Answer</summary>

256
</details>

<details>
<summary>Answer</summary>

A DOMAIN NAME
</details>

**Q: A DHT chord ring has 3 active peers; P1,P2 and P3. P1 has an address 20, P2 has an address 10 and P3 has an address 30. Which of the peers are responsible for the files with the following identifiers: 5,12,31 and 1?**

<details>
<summary>Answer</summary>

P1 holds 12, P2 holds 1,5 ,31
</details>

**Q: Threads share the same address sapce with other threads in the same process?**

<details>
<summary>Answer</summary>

True
</details>

**Q: Distribution transparency in multithreaded clients can be achieved by?**

<details>
<summary>Answer</summary>

1.using a convenient naming system 2. Hiding communication latency by using multiple threads for concurrent connections to server replicas.
</details>

<details>
<summary>Answer</summary>

It is possible to process requests concurrently without blocking the entire process.
</details>

<details>
<summary>Answer</summary>

Hiding communication latency by using multiple threads to concurrently connect to different replicas and fetch data.
</details>

<details>
<summary>Answer</summary>

The server can accept only one request at a time and can only accept new connection when it is done with processing the request.
</details>

**Q: Which of these statements about stateful and stateless servers are correct?**

<details>
<summary>Answer</summary>

1. Stateless server does not keep information about its client. 2. Stateful server keeps the state of its client.
</details>

<details>
<summary>Answer</summary>

Deaqling with redirection policy
</details>

<details>
<summary>Answer</summary>

1. Inconsistencies of states are reduced 2. Ease of horizontal scaling 3. Server can crash and recover with little overhead.
</details>

<details>
<summary>Answer</summary>

1. Marshalling and Unmarshalling of messages. 2. Interoperate between heretogenous platforms 3. Passing messages between the transport layer and the application layer
</details>

<details>
<summary>Answer</summary>

True
</details>

<details>
<summary>Answer</summary>

1. Byte ordering on the memories may be different because the hosts architectures in a distributed environment may be different 2. The processes operate in different memory address spaces in their respective hosts.
</details>

<details>
<summary>Answer</summary>

Allow a client process to execute a function on a remote server process.
</details>

<details>
<summary>Answer</summary>

Transient and synchronous communication.
</details>

<details>
<summary>Answer</summary>

1. Reduce communication latency by processing data close to where the data reside. 2. Achieve performance by distributing load where processes from heavily loaded machines are moved to lightly loaded machines. 3. Achieve flexibility by the client through dynamic download of the implementation of server-side interface.
</details>

<details>
<summary>Answer</summary>

The data sent by a sender is equal to the data received by the receiver and the order is preserved.
</details>

<details>
<summary>Answer</summary>

Demultiplexing
</details>

**Q: Is it possible for two processes running on different hosts to send UDP segments to the same prot on another host?**

<details>
<summary>Answer</summary>

True
</details>

**Q: What kind of packets are exchanged between protocol entities at the transport level?**

<details>
<summary>Answer</summary>

Segments
</details>

**Q: Assume that a host receives a UDP segment and finds that the checksum is correct. What does the receiver know?**

<details>
<summary>Answer</summary>

The segment received is equal to the segment sent with a very high probability.
</details>

**Q: Suppose you are given the following three 8-bit bytes: 01010011, 01100110, 00110100. What is the 1complement of the sum?**

<details>
<summary>Answer</summary>

00000000
</details>

**Q: Is it possible to deal with transmission errors on ACK/NAK segments in the RDT 2.0 protocol by simply retransmitting the current data segment in case a corrupt ACK or NAK is received by the sender?**

<details>
<summary>Answer</summary>

[Answer Missing]
</details>

**Q: Is it possible to avoid using NAK-segments in the RDT2.1 protocol by instead having sequence numbers in the acknowledgement – and still obtain a correct protocol?**

<details>
<summary>Answer</summary>

True
</details>

**Q: If the sender transport protocol entity in the RDT2.0 receives a corrupt ACK/NAK segment – what does the sender know for sure?**

<details>
<summary>Answer</summary>

Some segment was received by the receiver.
</details>

**Q: How is a TCP socket/ connection identified?**

<details>
<summary>Answer</summary>

By a tuple consisting of source port, source IP address, destination port, and destination IP address.
</details>

**Q: For which of the following transport protocols are acknowledgements cumulative?**

<details>
<summary>Answer</summary>

Go-back N
</details>

**Q: What is the purpose of flow control?**

<details>
<summary>Answer</summary>

To avoid that the sender overflows the receiver with data.
</details>

**Q: Loss of transport segments is always an indication of network congestion?**

<details>
<summary>Answer</summary>

False
</details>

**Q: What is the required relationship between the sequence number range and the windows size in the selective repeat protocol?**

<details>
<summary>Answer</summary>

The sequence number range must be at least twice the window size.
</details>

<details>
<summary>Answer</summary>

Vector clock
</details>

<details>
<summary>Answer</summary>

r1 = 2, s1= 1, a= 2, s2 = 3
</details>

<details>
<summary>Answer</summary>

r1 = (1 2 0),  e = (1 3 3)
</details>

**Q: Which of the mutual exclusion algorithms has N points of failure?**

<details>
<summary>Answer</summary>

Distributed.
</details>

<details>
<summary>Answer</summary>

True
</details>

<details>
<summary>Answer</summary>

1. accuracy is keeping the difference between the UTC and the clock for a machjne bound to a threshold value 2. Precision is keeping he deviation between the clocks of two machines in a distributed sy stem within a specified bound.
</details>

<details>
<summary>Answer</summary>

Processes can use the order of occurence of events rather than their absolute time occurences.
</details>

**Q: Given two Lamport’s logical clocks C(a) and C(b) corresponding to events a and b respectively. Which of the following statements can be true?**

<details>
<summary>Answer</summary>

1. If events a and b happen in the same process, and C(a) < C(b) then a->b
</details>

**Q: Given two events a and z, with Lamport clocks C(a) and C(z) and their vector clocks V(a) and V(z). What condition is necessary to conclude that event a happened before event z?**

2. If a is the sending of a message, and b is the receipt of that message. Then a->b and C(a) < C(b)
<details>
<summary>Answer</summary>

a happened before z if V(a) < V(z)
</details>

**Q: Which of the mutual exclusion algorithms require 2 (N-1) messages for a process to enter its critical region where N is the total number of processes?**

<details>
<summary>Answer</summary>

Distributed.
</details>

<details>
<summary>Answer</summary>

1. Increase reliability 2. Improve performance 3. Improve availability
</details>

<details>
<summary>Answer</summary>

1.Read and write patterns of the replicated data. 2. The purpose for which the data is used.
</details>

<details>
<summary>Answer</summary>

A way to measure and specify the level of inconsistencies that an application can tolerate.
</details>

<details>
<summary>Answer</summary>

Read your writes model
</details>

<details>
<summary>Answer</summary>

1. All write operations need to be forwarded to a single server 2. Operations are ordered in a sequential order. 3. Every data item has a primary server assigned to it.
</details>

<details>
<summary>Answer</summary>

Events have to be ordered across all replicas.
</details>

<details>
<summary>Answer</summary>

Quorum-based protocol.
</details>

<details>
<summary>Answer</summary>

True
</details>

<details>
<summary>Answer</summary>

Write operations can be performed at multiple replicas.
</details>

<details>
<summary>Answer</summary>

Proviidng consistency for a single client that accesses different replicas.
</details>

<details>
<summary>Answer</summary>

Updates can be performed in only one replica
</details>

<details>
<summary>Answer</summary>

It can survive when k processes fail.
</details>

**Q: What major problems can we face when client process crashes while its request has already been forwarded to the server for processing?**

<details>
<summary>Answer</summary>

1. The client’s request may creat orphan that may lock up files and tie up valuable resources 2. Old reply from the server can create confusion for the client when it reboots and sends a fresh request. 3. The client’s request may create orphan that may waste server’s CPU time.
</details>

<details>
<summary>Answer</summary>

Feedback implosion
</details>

**Q: How many processes are needed to form a byzantine agreement in a group with k faulty processes?**

<details>
<summary>Answer</summary>

It can continue to operate in the presence of faults.
</details>

<details>
<summary>Answer</summary>

1. Response failure 2. Byzantine failure
</details>

<details>
<summary>Answer</summary>

Organize several identical processes into a group.
</details>

**Q: A client can retransmit the request when dealing with lost reply messages from server to client. Which of the statements are correct?**

<details>
<summary>Answer</summary>

1. Server may not care abotu duplicate requests if the request is idempotent 2. Server needs to care about duplicate requests if the request is non-idempotent.
</details>

<details>
<summary>Answer</summary>

Receivers that received original emssage correctly have to process retransmitted messages that are useless to them.
</details>

**Q: How many processes are needed in a leaderless protocol to obtain a correct result from a majority vote in the event of crash or arbitrary failures by k processes?**

<details>
<summary>Answer</summary>

2k+1
</details>

**Q: What  service is provided by the network layer of the TCP/IP protocol stack?**

<details>
<summary>Answer</summary>

Unreliable end-to-end multi-hop transfer of datagrams between hosts.
</details>

**Q: How are IP addresses used in the Internet networking layer?**

<details>
<summary>Answer</summary>

IP addresses are assigned to network interfaces of hosts and network interfaces of routers.
</details>

**Q: What is the role of the forwarding function executed at the network layer?**

<details>
<summary>Answer</summary>

To transfer datagrams from icnoming links to the appropriate outgoing link.
</details>

**Q: What information can be found in a forwarding table of a router?**

<details>
<summary>Answer</summary>

Information about destination addresses and outgoing communication links.
</details>

**Q: What is the role of the routing function executed at the network layer?**

<details>
<summary>Answer</summary>

To compute the contents to be put into the forwarding tables of routers.
</details>

**Q: How many IP addresses are contained in the 223.1.1.0/23 CIDR-block fo addresses?**

<details>
<summary>Answer</summary>

512
</details>

<details>
<summary>Answer</summary>

b
</details>

**Q: What is the Dynamic Host Configuration Protocol being used for?**

<details>
<summary>Answer</summary>

To automatically configure a host network interface with an IP address.
</details>

**Q: Which of the following are examples of cloud computing service models?**

<details>
<summary>Answer</summary>

1. Infastructure as a service. 2. Software as a Service.
</details>

<details>
<summary>Answer</summary>

1. Storage 2. Network 3. Memory
</details>

<details>
<summary>Answer</summary>

Round robin
</details>

**Q: Virtual machines can be migrated from one host to another in a cloud environment?**

<details>
<summary>Answer</summary>

True
</details>

**Q: Which of the following cryptographic schemes can protect against spoofing OR What is the security solution to mitigate spoofing of distributed system servers?**

<details>
<summary>Answer</summary>

Digital signature.
</details>

**Q: Alice would like to digitally sign a message to be sent to Bob. What key should she use?**

<details>
<summary>Answer</summary>

Alice’s public key
</details>

**Q: Bob received a digitally signed message from Alice. What key should he use to verify the message?**

<details>
<summary>Answer</summary>

Alice’s public key
</details>

**Q: Bob would lik eto encrypt a message to be sent to Alice. What key should be used?**

<details>
<summary>Answer</summary>

Alice’s public key.
</details>

<details>
<summary>Answer</summary>

Certificate
</details>

**Q: Consider a network comprised of 10 routers(nodes) How many instances of Dijkstra’s algorithm do we need to execute to compute all the least-costs paths for the network?**

<details>
<summary>Answer</summary>

10
</details>

**Q: What is the purpose of the Address Resolution Protocol (ARP)?**

<details>
<summary>Answer</summary>

To find out which MAC address a host/router with a given IP address has
</details>

**Q: If we use an error detection technique (e.g. parity, checksum or CRC) then will we always catch a possible transmission error?**

<details>
<summary>Answer</summary>

False
</details>

**Q: On which type of communication link is there a need to use a link access protocol to coordinate access to communication?**

<details>
<summary>Answer</summary>

On a broadcast link
</details>

**Q: 2. Consider a network with three routers R1, R2, and R3 and the following cost function c(R1,R2) = 10 c(R1,R3) = 1 c(R2,R3) = 3 Assume that R1 has the following current distance vector R1 0 R2 10 R3 1 Assume that R3 has the following current distance vector R1 1 R2 3 R3 0 If R3 sends its distance vector to R1, how many entries in the distance vector of R1 will be updated?**

<details>
<summary>Answer</summary>

1
</details>

**Q: Which service provides link-level availability?**

<details>
<summary>Answer</summary>

Unreliable transmission of frames over a communication link.
</details>

<details>
<summary>Answer</summary>

One input for 0x3A
</details>

**Q: What is the purpose of "type" in the header of an Ethernet frame?**

<details>
<summary>Answer</summary>

To specify what upper-layer protocol is encapsulated in the data part of the frame.
</details>

**Q: Can frames collide when a hub is used to connect hosts/routers in a network?**

<details>
<summary>Answer</summary>

Yes
</details>

**Q: For which type(s) of random access protocol can collisions occur on the network OR For which type of medium access protocol may collision of frames occur?**

<details>
<summary>Answer</summary>

Carrier Sense with Multiple Access(CSMA)
</details>

**Q: What type of information is stored in an ARP table?**

<details>
<summary>Answer</summary>

Relationship between IP addresses and MAC addresses
</details>

**Q: Can loss of frames occur on an Ethernet switch?**

<details>
<summary>Answer</summary>

Yes
</details>

<details>
<summary>Answer</summary>

Omission failure
</details>

<details>
<summary>Answer</summary>

Infastructure as a Service
</details>

<details>
<summary>Answer</summary>

Platform as a service
</details>

**Q: What service does the link-layer of the TCP/IP protocol stack generally provide?**

<details>
<summary>Answer</summary>

Unreliable transmission of frames across one communication link.
</details>

<details>
<summary>Answer</summary>

Scalability
</details>

**Q: What security solution can be used to provide integrity and non-repudiation?**

<details>
<summary>Answer</summary>

Digital Signature
</details>

**Q: What security solution can provide non-repudiation?**

<details>
<summary>Answer</summary>

Digital signature based on asymmetric encryption.
</details>

**Q: Suppose we have a network that may duplicate datagrams, but where there are no transmissions errors, loss or overtaking. What protocol mechanism(s) are required to ensure reliable data transfer?**

<details>
<summary>Answer</summary>

Sequence numbers
</details>

## Oppgave 2 (10%)
**Q: 1.What is the main purpose of the ChordDHT system?**

<details>
<summary>Answer</summary>

Provide distributed and cooperative file sharing services where multiple providers of content cooperate to store and serve each other’s file and ensuring scalability, performance, high availability, and fault-tolerance.
</details>

**Q: 2.What is the main goal of the ChordDHT system?**

<details>
<summary>Answer</summary>

The main goal of ChordDHT is to provide distributed and cooperative file sharing services where multiple providers of content cooperate to store and serve each other’s’ data.
</details>

**Q: 3.How is the address size calculated?**

<details>
<summary>Answer</summary>

Using MD5 hash algorithm with 128bits. The address size is computed as 2128
</details>

**Q: 4.What entities are given addresses in the ChordDHT system?**

<details>
<summary>Answer</summary>

The server (processes) and files.
</details>

**Q: 5.What is the purpose of the finger table?**

<details>
<summary>Answer</summary>

To provide a routing table for efficiently and scalably resolving filename(keys) in O(log n) complexity.
</details>

**Q: 6.Multiple processes may want to update a file concurrently. Which approaches are used in project 3 for coordinating concurrent access by multiple processes that want to update the same file?**

<details>
<summary>Answer</summary>

Distributed mutual exclusion and Remote-write protocol.
</details>

<details>
<summary>Answer</summary>

In the ChordDHT, we define an address space of 2128 using MD5 hash algorithm. Files are replicated N times by appending index from 0 to N-1 to the file name. We then use the MD5 hash algorithm to give a unique identifier to each file replica. Similarly, we used the MD5 hash to give a unique name to each process. Identifier (replica) = Hash(replica) Identifier(process) = Hash(process)
</details>

<details>
<summary>Answer</summary>

2 methods: checkInterval and findHighestPredecessor Purposes: checkInterval is used to check if a key lies between the predecessor of a node and the node: pred(node) < key <= node. findHighestPredecessor is used to find the node that is closest (highest predecessor) to the key (node < finger < key) by searching from the bottom of the fingerTable (routing table)
</details>

**Q: 9.What type of sequential consistency protocol was implemented in Project 3?**

7. Explain briefly how processes and files are given names (identifiers) in the ChordDHT system.
8.The findSuccessor() method is used to lookup a key (file or process). What two methods are helper methods needed for findSuccessor() to work correctly? Briefly explain the purposes of these methods.
<details>
<summary>Answer</summary>

Remote write protocol (Primary-based protocol)
</details>

**Q: 10.What is the purpose of the findPrimaryOfItem() method in the FileManager class and what is the returned primary used for?**

<details>
<summary>Answer</summary>

The method is used to find which of the returned processes is the primary process. The returned primary is used to coordinate writes to other replicas.
</details>

**Q: 11. In which of the tasks in Project 3 was LamportClock used? And for what purpose was it used?**

<details>
<summary>Answer</summary>

LamportClock was used in the distributed mutual exclusion algorithm task. The Lamport clock was used to provide timestamps and total ordering to the messages exchanged by the processes. Using the Lamport timestamps, processes can decide which process enters the critical region based on the lower timestamp.
</details>

<details>
<summary>Answer</summary>

Embedded microprocessor/controller and software, dedicated purpose and interface, sensors and actuators
</details>

<details>
<summary>Answer</summary>

PIR sensor, push bottons, leds
</details>

<details>
<summary>Answer</summary>

The setup()-function is executed upon start/boot of the device and is typically used for initialisation purposes. The loop()-function is repeatedly executed and typically consist of reading sensors, processing data, and controlling actuators.
</details>

**Q: 4.Which hardware component of an IoT device is responsible for executing the software/program embedded on the device?**

1.Explain briefly what characterises an IoT device.
2.Specify which sensors and which actuators that were being used on the access control IoT device in project 4.
3.Explain briefly the main purpose of the setup()-function and the loop()-function in an Arduino program.
<details>
<summary>Answer</summary>

The microprocessor/controller
</details>

<details>
<summary>Answer</summary>

The Spark/Java service has to be augmented such that a delete request containing an identifier will be processed. Handling of the identifier can be done in a similar way as when handling a get request for a specific entry in the access log. In the method handling the new delete request, the entry can be delete from the hash-map storing the entries in the access log.
</details>

<details>
<summary>Answer</summary>

The three levels that to be implemented were: IoT application layer, RPC layer, and Messaging layer. The messaging layer was implemented on top of TCP and was used to implement the RPC layer for remote-procedure calls. The RPC layer was then used by the IoT application layer to implement the sensor-display-controller IoT system at the application layer.
</details>

<details>
<summary>Answer</summary>

The first 8 bits is used to specify the number of payload bytes containing data in the subsequent 127 bytes. It is needed because the messages have a fixed length of 128 bytes leaving room for up to 127 bytes of data. But not all messages will have 127 of payload data.
</details>

**Q: 3.The Java socket API and the TCP transport service was used in the implementation. What two elements are being used to identify a socket (communication endpoint) at the transport layer of the TCP/IP protocol stack?**

5.The cloud service implemented in the project using the Spark/Java framework made it possible for the access control device to send an HTTP DELETE request with the URL /accessdevice/log/ to delete all entries in the access log. Explain how you would extend the cloud service such that it would be possible to delete a specific entry in the access log. Socket Programming and RPC middleware (Oblig 1)
1.List the three protocol layers that were implemented in the project and explain briefly how they are related.
2.The messages exchanged in task 1 of the project has a fixed length of 128 bytes. Briefly explain the purpose of the first 8 bits in the messages and why they are needed.
<details>
<summary>Answer</summary>

A socket represents a communication endpoint and is identified using a port number and an IP address.
</details>

**Q: 4.In Task 2 of the project: when the server receives an RPC request from a client, how does the server identify the method to be invoked?**

<details>
<summary>Answer</summary>

The first byte of an RPC request message which is carried as payload data in the fixedsized messages at the messaging layer is used to specify the number of the RPC method. This number is then used to lookup the method in the RPC table on the RPC server.
</details>

<details>
<summary>Answer</summary>

Main components of the broker were Messaging Server (implementing the underlying messaging service used to receive messages from clients), Broker (which implements a loop to handle clients that connect to the broker), Dispatcher (which processes the various messages that can be received), Storage (which stores information about clients that are connected and which clients subscribe to which topics).
</details>

**Q: 2. The publish-subscribe messaging middleware was implemented on top of a messaging layer. What was the service provided by this messaging layer?**

1.List the main components that were implemented in the Broker and explain briefly their purpose.
<details>
<summary>Answer</summary>

The messaging layer builds a messaging abstraction on top of TCP that enables a client and a server reliably exchanging (short) messages).
</details>

**Q: 3. When the broker receives a publish message from a client it needs to find out what clients is to receive the message. Explain briefly how the broker identifies the clients to which the message should be sent?**

<details>
<summary>Answer</summary>

This is done via Storage which has a HashMap which for each topic (key) topic stores the list of the clients (users, values)) who subscribe to this topic.
</details>

<details>
<summary>Answer</summary>

Stopable is built on Threads and has a run method that continuously runs a doProcess method until The doStop method is called. By implementing the doProcess method, one can make the thread continuously perform a task.
</details>

<details>
<summary>Answer</summary>

The broker must be changed so that in the WaitConnect method it creates a new dispatcher thread for the client that connects. This thread will then handle requests from the client
</details>

## Oppgave 7 (5%)
**Q: 1.What is the purpose of using multithreading and callback mechanisms in RPC design?**

4. Some of the software components in the publish-subscribe middleware were implemented using the Stopable-thread abstraction. Explain briefly how a Stopablethread works and what kind of task it can be used for. Sketch briefly how the broker could be extended such that it is possible to process multiple client sessions in parallel, i.e., exploit that the server may have multiple cores
<details>
<summary>Answer</summary>

The main goal is to avoid blocking by constructing an asynchronous RPC and thereby allow the processes to continue running.
</details>

**Q: 2. What is failure transparency?**

<details>
<summary>Answer</summary>

failure transparency is about hiding the failure and recovery of object. Means that a user or application does not notice that some part of the software fails to work properly, and that the system subsequently (automatically) recovers from that failure.
</details>

<details>
<summary>Answer</summary>

Distribution transparency is about how to achieve the single-system image, i.e., how to make a collection of networked computers and processes appear as a single computer and process.
</details>

<details>
<summary>Answer</summary>

In multi-threaded server request from client is passed to separate thread to process the request. In this way, the server can handle multiple requests. Multithreading also allows server to exploit multi-processor architectures leading to better performance.
</details>

**Q: 5. What are the various types of distribution transparency?**

3. Describe briefly what distribution transparency mean in distributed system design.
4.Explain briefly the main use of multi-threading in server design.
<details>
<summary>Answer</summary>

Access transparency: Hide differences in data representation and how an object is accessed. Location transparency: Hide where an object is located. Relocation transparency: Hide that object may be moved to another location while in use. Migration transparency: Hide movement of object to another location. Replication transparency: Hide replication of object. Concurrency transparency: Hide the sharing of object by several independent users. Failure transparency: Hide the failure & recovery of an object.
</details>

<details>
<summary>Answer</summary>

The traditional RPC is a synchronous, blocking communication model where the sender and the receiver must be running for the call to succeed. Whereas the message-oriented communication model is asynchronous and non-blocking communication model. It allows communication between the sender and the receiver to be loosely coupled in time (e.g., by using brokers).
</details>

**Q: 7.Describe briefly the difference between stateful and stateless servers?**

6. Explain briefly the difference between traditional remote procedure call (RPC) communication model and message-oriented communication model.
<details>
<summary>Answer</summary>

Stateful servers maintain persistent information about their clients while stateless servers do not keep information about the state of its client and can change its own state without having to inform any client.
</details>

**Q: 8. Describe briefly the difference between synchronous and asynchronous communication?**

<details>
<summary>Answer</summary>

In synchronous communication, the sender is blocked until its request is known to be accepted. In asynchronous communication, sender continues immediately (not blocked) after it has submitted its message for transmission.
</details>

<details>
<summary>Answer</summary>

Multi-threading allows server to handle multiple requests from clients without blocking. Multithreading also allows server to exploit multi-processor architectures leading to better performance.
</details>

<details>
<summary>Answer</summary>

Access transparency deals with hiding differences in data representation and the way that objects can be accessed between distributed systems.
</details>
