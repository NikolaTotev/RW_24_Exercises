import 'package:flutter/material.dart';

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
          )
        ]);
  }
}

// Exercise 1 - Create a button
Widget createButton() {
  return FloatingActionButton(
    onPressed: () {
      print("The button was pressed!");
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

// Widget create_textbox() {
//   return ...
// }


