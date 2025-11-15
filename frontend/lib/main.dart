import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

import 'package:frontend/pages/ai_image_detector_page.dart';
import 'package:frontend/pages/ai_video_detector_page.dart';
import 'package:frontend/pages/home_page.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ForensIQ Vision',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => const HomePage(),
        '/ai_image_detector': (context) => const AiImageDetectorPage(),
        '/ai_video_detector': (context) => const AiVideoDetectorPage(),
      },
    );
  }
}
