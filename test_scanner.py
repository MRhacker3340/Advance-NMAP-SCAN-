#!/usr/bin/env python3
"""
Test Suite for Advanced Nmap Scanner
Validates all major functionality
"""

import subprocess
import sys
import os
import time

def run_test(description, command, expected_success=True):
    """Run a test command and verify results"""
    print(f"\n🧪 Testing: {description}")
    print("-" * 50)
    
    try:
        start_time = time.time()
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        end_time = time.time()
        
        if expected_success and result.returncode == 0:
            print(f"✅ PASS - Completed in {end_time - start_time:.2f}s")
            return True
        elif not expected_success and result.returncode != 0:
            print(f"✅ PASS - Expected failure occurred")
            return True
        else:
            print(f"❌ FAIL - Return code: {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT - Test took too long")
        return False
    except Exception as e:
        print(f"❌ EXCEPTION - {str(e)}")
        return False

def main():
    print("🚀 Advanced Nmap Scanner Test Suite")
    print("=" * 60)
    
    scanner_path = os.path.join(os.path.dirname(__file__), 'advanced_nmap_scanner.py')
    
    if not os.path.exists(scanner_path):
        print(f"❌ Scanner not found at: {scanner_path}")
        sys.exit(1)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Help output
    total_tests += 1
    if run_test("Help output", [
        'python3', scanner_path, '--help'
    ]):
        tests_passed += 1
    
    # Test 2: Invalid target handling
    total_tests += 1
    if run_test("Invalid target handling", [
        'python3', scanner_path, '-t', 'invalid..target', '--quick', '--no-banner'
    ], expected_success=False):
        tests_passed += 1
    
    # Test 3: Host discovery on localhost
    total_tests += 1
    if run_test("Host discovery scan", [
        'python3', scanner_path, '-t', '127.0.0.1', '--host-discovery', '--no-banner'
    ]):
        tests_passed += 1
    
    # Test 4: Quick scan on localhost
    total_tests += 1
    if run_test("Quick scan", [
        'python3', scanner_path, '-t', '127.0.0.1', '--quick', '--no-banner'
    ]):
        tests_passed += 1
    
    # Test 5: Specific port scan
    total_tests += 1
    if run_test("Specific port scan", [
        'python3', scanner_path, '-t', '127.0.0.1', '--ports', '22,80', '--no-banner'
    ]):
        tests_passed += 1
    
    # Test 6: Stealth scan
    total_tests += 1
    if run_test("Stealth scan", [
        'python3', scanner_path, '-t', '127.0.0.1', '--stealth', '--ports', '22,80', '--no-banner'
    ]):
        tests_passed += 1
    
    # Test 7: Default behavior (no scan type specified)
    total_tests += 1
    if run_test("Default behavior", [
        'python3', scanner_path, '-t', '127.0.0.1', '--no-banner'
    ]):
        tests_passed += 1
    
    # Test 8: File saving functionality
    total_tests += 1
    if run_test("Save results to file", [
        'python3', scanner_path, '-t', '127.0.0.1', '--quick', '--save-results', '--no-banner'
    ]):
        tests_passed += 1
    
    # Test utility scripts
    quick_scan_path = os.path.join(os.path.dirname(__file__), 'quick_scan.py')
    if os.path.exists(quick_scan_path):
        total_tests += 1
        if run_test("Quick scan utility", [
            'python3', quick_scan_path, '127.0.0.1'
        ]):
            tests_passed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    print(f"Tests Passed: {tests_passed}/{total_tests}")
    print(f"Success Rate: {(tests_passed/total_tests)*100:.1f}%")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! The scanner is working correctly.")
        return 0
    else:
        print("⚠️ Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())