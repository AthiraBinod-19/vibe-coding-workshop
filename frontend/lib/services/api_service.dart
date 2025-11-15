import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String _baseUrl = 'http://127.0.0.1:8000'; // Replace with your backend URL

  Future<Map<String, dynamic>> detectAiImage(String imagePath) async {
    // Placeholder for API call
    print('Detecting AI image...');
    await Future.delayed(const Duration(seconds: 2));
    return {
      'is_ai_generated': true,
      'confidence': 0.85,
      'detected_artifacts': ['diffusion noise', 'upscaler patterns'],
      'heatmap': '',
      'explanation': 'This is a placeholder explanation.',
    };
  }

  Future<Map<String, dynamic>> detectAiVideo(String videoPath) async {
    // Placeholder for API call
    print('Detecting AI video...');
    await Future.delayed(const Duration(seconds: 5));
    return {
      'is_ai_generated': true,
      'manipulation_type': 'deepfake face swap',
      'confidence': 0.92,
      'suspicious_frames': [10, 25, 42],
      'sample_heatmap': '',
      'explanation': 'This is a placeholder explanation.',
    };
  }
}
