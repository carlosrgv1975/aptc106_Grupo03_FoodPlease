import { Component, OnInit } from '@angular/core';
import { FoodpleaseApiService } from '../core/services/foodplease-api.service';
import { Local } from '../core/models/foodplease.models';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  standalone: false,
})
export class Tab1Page implements OnInit {
  locales: Local[] = [];
  cargando = true;
  error: string | null = null;

  constructor(private api: FoodpleaseApiService) {}

  ngOnInit(): void {
    this.cargarLocales();
  }

  cargarLocales(): void {
    this.cargando = true;
    this.error = null;
    this.api.getLocales().subscribe({
      next: (data) => {
        this.locales = data;
        this.cargando = false;
      },
      error: (err) => {
        this.error = 'No fue posible cargar los restaurantes. Verifica que el backend Flask esté corriendo en http://127.0.0.1:5000.';
        this.cargando = false;
        console.error('Error al cargar locales:', err);
      },
    });
  }

  iconoRubro(rubro: string): string {
    const r = (rubro || '').toLowerCase();
    if (r.includes('pizz')) return 'pizza';
    if (r.includes('hambur') || r.includes('rapid')) return 'fast-food';
    if (r.includes('sushi') || r.includes('japon')) return 'fish';
    if (r.includes('postre') || r.includes('dulce')) return 'ice-cream';
    if (r.includes('bebid') || r.includes('jugo')) return 'cafe';
    return 'restaurant';
  }
}
