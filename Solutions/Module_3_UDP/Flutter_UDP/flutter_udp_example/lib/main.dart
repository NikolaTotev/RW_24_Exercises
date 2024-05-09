import 'package:flutter/material.dart';
import 'package:flutter_udp_example/udp_streamer.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Ocadi GUI',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
          useMaterial3: true,
        ),
        home: Scaffold(body: Center(child: Homepage())));
  }
}

class Homepage extends StatelessWidget {
  UdpStreamer streamer = UdpStreamer();
  String robotIp = '192.168.4.1';
  int robotPort = 2390;

  Homepage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
        //Some code to make things look nicer
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,

        //The actual UI elements
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: createButton(),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: createText(),
          ),
          TextBox(streamer: streamer)
        ]);
  }

// Exercise 1 - Create a button
  Widget createButton() {
    return FloatingActionButton(
      onPressed: () {
        print("The button was pressed!");
        streamer.sendData("Button Pressed", robotIp, robotPort);
      },
      tooltip: 'Increment',
      child: const Icon(Icons.add),
    );
  }

// Exercise 1 - Create a text label
  Widget createText() {
    return const Text(
      "This is my text",

      //Some more code to make things nicer.
      textAlign: TextAlign.center,
      style: TextStyle(fontSize: 24.0, fontWeight: FontWeight.bold),
    );
  }
}

// Define a custom textbox widget.
class TextBox extends StatefulWidget {
  TextBox({super.key, required this.streamer});
  UdpStreamer streamer;
  String robotIp = '192.168.4.1';
  int robotPort = 2390;

  @override
  State<TextBox> createState() => _TextBoxState();
}

// Define a corresponding State class.
// This class holds the data related to the textbox.
class _TextBoxState extends State<TextBox> {
  // Create a text controller and use it to retrieve the current value
  // of the TextField.
  final textInputController = TextEditingController();

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    textInputController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.only(
              top: 20.0, bottom: 20.0, left: 50.0, right: 50.0),
          child: TextField(controller: textInputController),
        ),
        Padding(
          padding: const EdgeInsets.all(20.0),
          child: ElevatedButton(
              onPressed: () {
                print(textInputController.text);
                widget.streamer.sendData(textInputController.text,widget.robotIp, widget.robotPort );
              },
              child: const Text("Print Data")),
        )
      ],
    );
  }
}
