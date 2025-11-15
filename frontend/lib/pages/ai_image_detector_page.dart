import 'package:flutter/material.dart';

class AiImageDetectorPage extends StatefulWidget {
  const AiImageDetectorPage({super.key});

  @override
  State<AiImageDetectorPage> createState() => _AiImageDetectorPageState();
}

class _AiImageDetectorPageState extends State<AiImageDetectorPage> {
  bool _isLoading = false;
  String _result = '';

  void _detectAiImage() {
    setState(() {
      _isLoading = true;
    });

    // Simulate API call
    Future.delayed(const Duration(seconds: 2), () {
      setState(() {
        _isLoading = false;
        _result = 'AI-generated: Yes\nConfidence: 85%';
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('AI Photo Detector'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              onPressed: _detectAiImage,
              child: const Text('Upload Image'),
            ),
            const SizedBox(height: 20),
            if (_isLoading)
              const CircularProgressIndicator()
            else
              Text(_result),
          ],
        ),
      ),
    );
  }
}
