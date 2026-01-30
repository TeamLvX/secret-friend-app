"""
Debug utilities for the application.

This module provides debugging helpers that can be used throughout the application.
Use `wait_for_debugger()` to pause execution and wait for a debugger to attach.
"""

import os
import sys


def wait_for_debugger(host: str = "0.0.0.0", port: int = 5678) -> None:
    """
    Wait for a debugger to attach before continuing execution.

    This function will pause execution and wait for a debugger to attach.
    The debugger should connect to the specified host and port.

    Usage:
        from src.core.debug import wait_for_debugger

        # In your code where you want to break:
        wait_for_debugger()
        # Your code here will only execute after debugger attaches

    Args:
        host: The host to listen on (default: "0.0.0.0" for all interfaces)
        port: The port to listen on (default: 5678)

    Example:
        >>> from src.core.debug import wait_for_debugger
        >>> wait_for_debugger(port=5678)
        # Execution will pause here until debugger attaches
    """
    try:
        import debugpy

        if not debugpy.is_client_connected():
            print(f"Waiting for debugger to attach on {host}:{port}...")
            print("In VS Code/Cursor: Use 'Python: Attach' debug configuration")
            debugpy.listen((host, port))
            debugpy.wait_for_client()
            print("Debugger attached! Continuing execution...")
        else:
            print("Debugger already attached.")
    except ImportError:
        print(
            "debugpy not installed. Install it with: pip install debugpy",
            file=sys.stderr,
        )
        print("Skipping debugger attachment...", file=sys.stderr)


def start_debug_server(host: str = "0.0.0.0", port: int = 5678) -> None:
    """
    Start a debug server that will wait for a debugger to attach.

    This is similar to wait_for_debugger() but doesn't block execution.
    Use this at the start of your application to enable debugging.

    Args:
        host: The host to listen on (default: "0.0.0.0")
        port: The port to listen on (default: 5678)
    """
    try:
        import debugpy

        if not debugpy.is_client_connected():
            debugpy.listen((host, port))
            print(f"Debug server started on {host}:{port}")
            print("Waiting for debugger to attach...")
            print("In VS Code/Cursor: Use 'Python: Attach' debug configuration")
        else:
            print("Debug server already running.")
    except ImportError:
        print(
            "debugpy not installed. Install it with: pip install debugpy",
            file=sys.stderr,
        )


def should_enable_debug() -> bool:
    """
    Check if debugging should be enabled based on environment variables.

    Returns:
        True if DEBUG environment variable is set to a truthy value
    """
    debug_env = os.getenv("DEBUG", "false").lower()
    return debug_env in ("true", "1", "yes", "on")


def setup_debugging_if_enabled(host: str = "0.0.0.0", port: int = 5678) -> None:
    """
    Set up debugging if DEBUG environment variable is enabled.

    This is a convenience function that checks the DEBUG env var and
    starts the debug server if enabled.

    Args:
        host: The host to listen on (default: "0.0.0.0")
        port: The port to listen on (default: 5678)
    """
    if should_enable_debug():
        start_debug_server(host, port)
