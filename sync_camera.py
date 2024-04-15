# Description: This script demonstrates how to synchronize the camera view between two Open3D visualizers.
# Currently this script only supports synchronization of the camera view of the "Visualizer 2" window to the "Visualizer 1" window.

import open3d as o3d

def make_box(color):
    box = o3d.geometry.TriangleMesh.create_box(width=1, height=2, depth=4)
    box.paint_uniform_color(color)  # Set color to differentiate the two boxes
    return box

def synchronize_views(source_vis, target_vis):
    # Retrieve the view control parameters from the source visualizer
    source_view = source_vis.get_view_status()
    
    # Apply the view control parameters to the target visualizer
    target_vis.set_view_status(source_view)
    target_vis.update_renderer()

def main():
    # Create two visualizers
    vis1 = o3d.visualization.VisualizerWithKeyCallback()
    vis2 = o3d.visualization.VisualizerWithKeyCallback()

    vis1.create_window(window_name='Visualizer 1', width=800, height=600)
    vis2.create_window(window_name='Visualizer 2', width=800, height=600)

    # Create two point clouds and add them to the respective visualizers
    box1 = make_box([1, 0, 0])  # Red box
    box2 = make_box([0, 0, 1])  # Blue box
    
    vis1.add_geometry(box1)
    vis2.add_geometry(box2)

   # Define a key callback to synchronize view from vis1 to vis2
    def key_callback(vis):
        if vis.get_window_name == 'Visualizer 1':
            synchronize_views(vis1, vis2)
        else:
            synchronize_views(vis2, vis1)
        return False

    # Register the key callback with 'vis1' and 'vis2' for the 'S' key
    vis1.register_key_callback(ord('S'), key_callback)
    vis2.register_key_callback(ord('S'), key_callback)


    # Start the visualization in a loop
    while True:
        vis1.poll_events()
        vis1.update_renderer()
        vis2.poll_events()
        vis2.update_renderer()

if __name__ == "__main__":
    main()
