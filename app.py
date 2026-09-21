import folium
import os

def create_sih_map():
    # 1. Initialize the map centered around India (or a specific landslide-prone area)
    # Using Uttarakhand coordinates as an example center
    map_center = [30.0668, 79.0193]
    
    # Create the base map without default openstreetmap tiles
    sih_map = folium.Map(
        location=map_center, 
        zoom_start=7, 
        tiles=None # We will add custom Google Map tiles manually below
    )

    # 2. Define Google Maps Tilesets
    google_roadmap = folium.TileLayer(
        tiles='https://google.com{x}&y={y}&z={z}',
        attr='Google Roadmap',
        name='Google Maps (Roadmap)',
        overlay=False,
        control=True
    )
    
    google_satellite = folium.TileLayer(
        tiles='https://google.com{x}&y={y}&z={z}',
        attr='Google Satellite',
        name='Google Maps (Satellite)',
        overlay=False,
        control=True
    )
    
    google_terrain = folium.TileLayer(
        tiles='https://google.com{x}&y={y}&z={z}',
        attr='Google Terrain',
        name='Google Maps (Terrain)',
        overlay=False,
        control=True
    )
    
    google_hybrid = folium.TileLayer(
        tiles='https://google.com{x}&y={y}&z={z}',
        attr='Google Hybrid',
        name='Google Maps (Hybrid)',
        overlay=False,
        control=True
    )

    # Add Google layers to the map
    google_roadmap.add_to(sih_map)
    google_satellite.add_to(sih_map)
    google_terrain.add_to(sih_map)
    google_hybrid.add_to(sih_map)

    # 3. SIH26001 Context: Add Sample Dynamic Landslide Risk Mock Data
    # For a real project, replace this with your AI/ML model outputs (SAR, rainfall, soil moisture)
    landslide_hotspots = [
        {"name": "Joshimath Region", "coords": [30.5524, 79.5663], "risk": "High", "color": "red"},
        {"name": "Rudraprayag Zone", "coords": [30.2844, 78.9811], "risk": "Medium", "color": "orange"},
        {"name": "Uttarkashi Zone", "coords": [30.7268, 78.4354], "risk": "Low", "color": "green"}
    ]

    for spot in landslide_hotspots:
        # Create HTML popup with dynamic info matching the SIH26001 theme
        html_popup = f"""
        <div style="font-family: Arial, sans-serif; width: 200px;">
            <h4><b>{spot['name']}</b></h4>
            <hr style="margin: 5px 0;">
            <p><b>SIH26001 Tracker</b></p>
            <p>Risk Level: <span style="color:{spot['color']}; font-weight:bold;">{spot['risk']}</span></p>
            <p><small>Monitored via Satellite SAR & Rainfall Indicators</small></p>
        </div>
        """
        
        # Add visual markers
        folium.CircleMarker(
            location=spot['coords'],
            radius=12,
            popup=folium.Popup(html_popup, max_width=250),
            color=spot['color'],
            fill=True,
            fill_color=spot['color'],
            fill_opacity=0.6
        ).add_to(sih_map)

    # 4. Add a Layer Control Panel (This creates the top-right toggle option exactly like Google Maps)
    folium.LayerControl(position='topright').add_to(sih_map)

    # 5. Save map to an HTML file to render in browser
    output_file = "sih26001_google_map_view.html"
    sih_map.save(output_file)
    print(f"Map successfully created! Open '{output_file}' in your web browser to view your Google Map pipeline.")

if __name__ == "__main__":
    create_sih_map()
