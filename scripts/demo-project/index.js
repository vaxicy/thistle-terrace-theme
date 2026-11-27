// Thistle & Terrace Theme — thistle purple over a sage terrace
import { readFile } from 'node:fs/promises';

const PALETTE = {
  thistle: '#7E4E88',
  lilac: '#AF8EB1',
  sage: '#ACCFC5',
  cream: '#F1E3C4',
  plum: '#301A2A',
  ink: '#2B1C2F',
};

export class Terrace {
  constructor(name = 'North terrace') {
    this.name = name;
    this.palette = PALETTE;
    this.tones = Object.keys(PALETTE).filter((k) => k !== 'ink');
  }

  blend(from, to, ratio = 0.5) {
    const parse = (hex) => [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    return '#' + a.map((v, i) => Math.round(v * (1 - ratio) + b[i] * ratio)
      .toString(16).padStart(2, '0')).join('');
  }

  async readTerrace(file) {
    const content = await readFile(file, 'utf8');
    return { name: this.name, tones: this.tones.length,
             lines: content.split('\n').filter(Boolean).length, content };
  }
}

const terrace = new Terrace();
console.log(`terrace wash: ${terrace.blend(PALETTE.thistle, PALETTE.sage)}`);
