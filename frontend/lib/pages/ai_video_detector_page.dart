import 'package:flutter/material.dart';

class AiVideoDetectorPage extends StatefulWidget {
  const AiVideoDetectorPage({super.key});

  @override
  State<AiVideoDetectorPage> createState() => _AiVideoDetectorPageState();
}

class _AiVideoDetectorPageState extends State<AiVideoDetectorPage> {
  bool _isLoading = false;
  String _result = '';

  void _detectAiVideo() {
    setState(() {
      _isLoading = true;
    });

    // Simulate API call
    Future.delayed(const Duration(seconds: 5), () {
      setState(() {
        _isLoading = false;
        _result = 'AI-generated: Yes\nManipulation Type: Deepfake Face Swap\nConfidence: 92%';
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('AI Video Detector'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              onPressed: _detectAiVideo,
              child: const Text('Upload Video'),
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
