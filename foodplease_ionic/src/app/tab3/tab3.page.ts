import { Component, OnInit } from '@angular/core';
import { FoodpleaseApiService } from '../core/services/foodplease-api.service';
import { Cliente, Metrics } from '../core/models/foodplease.models';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
  standalone: false,
})
export class Tab3Page implements OnInit {
  cliente: Cliente | null = null;
  metrics: Metrics | null = null;
  cargando = true;
  error: string | null = null;

  constructor(private api: FoodpleaseApiService) {}

  ngOnInit(): void {
    this.cargar();
  }

  cargar(): void {
    this.cargando = true;
    this.error = null;
    // Auto-login al primer cliente seed para demostración de flujo
    this.api.login().subscribe({
      next: (resp) => {
        this.cliente = resp.cliente;
        // Después del login, traemos las métricas del sistema
        this.api.getMetrics().subscribe({
          next: (data) => {
            this.metrics = data;
            this.cargando = false;
          },
          error: () => {
            this.cargando = false;
          },
        });
      },
      error: (err) => {
        this.error = 'No fue posible cargar el perfil. Verifica que el backend Flask esté corriendo.';
        this.cargando = false;
        console.error('Error al cargar perfil:', err);
      },
    });
  }
}
